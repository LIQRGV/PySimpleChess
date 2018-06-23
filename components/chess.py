import re

from exceptions import (
    InvalidCodeException,
    InvalidMoveException,
    InvalidPieceException,
    KillingOwnPieceException,
    PieceMoveNotAllowedException,
)
from .pieces import (
    Pawn, Rook, Knight,
    Bishop, Queen, King,
)
from .piece_side import PieceSide

class Chess:
    class _Coordinate:
        def __init__(self, x, y):
            self.x = x
            self.y = y

    class _PieceInfo:
        def __init__(self, piece_side, piece_type):
            self.piece_side = piece_side
            self.piece_type = piece_type

    def __init__(self):
        self.position = self.__initialize_position()
        valid_pattern = "([a-h])([1-8])"
        compiled_re = re.compile(valid_pattern)
        self.__code_matcher = compiled_re.match

    def __initialize_position(self):
        board = [
            [None for _ in range(8)] for _ in range(8)
        ]
        # rook
        rook_positions_and_side = [
            ([0, 0], PieceSide.WHITE), ([0, 7], PieceSide.WHITE),
            ([7, 0], PieceSide.BLACK), ([7, 7], PieceSide.BLACK),
        ]
        # knight
        knight_positions_and_side = [
            ([0, 1], PieceSide.WHITE), ([0, 6], PieceSide.WHITE),
            ([7, 1], PieceSide.BLACK), ([7, 6], PieceSide.BLACK),
        ]
        # bishop
        bishop_positions_and_side = [
            ([0, 2], PieceSide.WHITE), ([0, 5], PieceSide.WHITE),
            ([7, 2], PieceSide.BLACK), ([7, 5], PieceSide.BLACK),
        ]
        # king
        king_positions_and_side = [
            ([0, 3], PieceSide.WHITE),
            ([7, 3], PieceSide.BLACK),
        ]
        # queen
        queen_positions_and_side = [
            ([0, 4], PieceSide.WHITE),
            ([7, 4], PieceSide.BLACK),
        ]
        # pawn
        pawn_positions_and_side = [
            *[([1, pos], PieceSide.WHITE) for pos in range(0, 8)],
            *[([6, pos], PieceSide.BLACK) for pos in range(0, 8)],
        ]

        for PieceTypeClass, positions_and_side in [
            (Rook, rook_positions_and_side),
            (Knight, knight_positions_and_side),
            (Bishop, bishop_positions_and_side),
            (Queen, queen_positions_and_side),
            (King, king_positions_and_side),
            (Pawn, pawn_positions_and_side),
        ]:
            for coordinate, side in positions_and_side:
                x = coordinate[0]
                y = coordinate[1]
                piece = PieceTypeClass()
                piece_info = self._PieceInfo(side, piece)
                board[x][y] = piece_info

        return board

    def move(self, playing_side, starting_code, destination_code):
        match_codes = [
            self.__code_matcher(code) for code in [starting_code, destination_code]
        ]

        for code in match_codes:
            if code is None:
                raise InvalidCodeException()

        starting_re_match = match_codes[0]
        starting_x_pos = ord(starting_re_match.group(1)) - ord('a')
        starting_y_pos = int(starting_re_match.group(2)) - 1

        destination_re_match = match_codes[1]
        destination_x_pos = ord(destination_re_match.group(1)) - ord('a')
        destination_y_pos = int(destination_re_match.group(2)) - 1

        piece_info = self.position[starting_y_pos][starting_x_pos]

        if piece_info is None:
            raise InvalidPieceException()

        start_position = self._Coordinate(starting_x_pos, starting_y_pos)
        target_position = self._Coordinate(destination_x_pos, destination_y_pos)

        piece_side = piece_info.piece_side
        piece_type = piece_info.piece_type

        if piece_side != playing_side:
            raise PieceMoveNotAllowedException()

        is_obstructed = self.__is_obstructed(start_position, target_position)
        is_killing = self.__is_killing(target_position, playing_side)
        is_backward = self.__is_backward(start_position, target_position, playing_side)

        if piece_type.can_move(start_position, target_position, is_obstructed, is_killing, is_backward):
            self.position[starting_y_pos][starting_x_pos] = None
            self.position[destination_y_pos][destination_x_pos] = piece_info
        else:
            raise InvalidMoveException()

    def __is_obstructed(self, start_pos, target_pos):
        is_diagonal = lambda pos1, pos2: abs(pos1.x - pos2.x) == abs(pos1.y - pos2.y)
        is_straight = lambda pos1, pos2: pos1.x == pos2.x or pos1.y == pos2.y
        path_to_check = []
        if is_diagonal(start_pos, target_pos):
            x_modifier = 1 if start_pos.x < target_pos.x else -1
            range_x = range(start_pos.x + x_modifier, target_pos.x, x_modifier)
            y_modifier = 1 if start_pos.y < target_pos.y else -1
            range_y = range(start_pos.y + y_modifier, target_pos.y, y_modifier)
            path_to_check = zip(range_x, range_y)
        elif is_straight(start_pos, target_pos):
            if start_pos.x == target_pos.x:
                min_y_val = min(start_pos.y, target_pos.y)
                max_y_val = max(start_pos.y, target_pos.y)
                path_to_check = [(start_pos.x, i) for i in range(min_y_val + 1, max_y_val)]
            else:
                min_x_val = min(start_pos.x, target_pos.x)
                max_x_val = max(start_pos.x, target_pos.x)
                path_to_check = [(i, start_pos.y) for i in range(min_x_val + 1, max_x_val)]

        for coordinate in path_to_check:
            x = coordinate[0]
            y = coordinate[1]
            if self.position[y][x] is not None:
                return True

        return False

    def __is_killing(self, target_pos, playing_side):
        x = target_pos.x
        y = target_pos.y
        occupant = self.position[y][x]

        if occupant is None:
            return False
        elif occupant.piece_side != playing_side:
            return True

        raise KillingOwnPieceException()

    def __is_backward(self, current_pos, target_pos, playing_side):
        return (current_pos.y < target_pos.y) ^ (playing_side == PieceSide.WHITE)

