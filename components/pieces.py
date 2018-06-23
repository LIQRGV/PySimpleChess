class Rook:
    def __str__(self):
        return "Rook"

    def can_move(self, start_pos, target_pos, obsctructed, is_killing, is_backward):
        if obsctructed:
            return False
        if((start_pos.x == target_pos.x and start_pos.y != target_pos.y) or
                (start_pos.x != target_pos.x and start_pos.y == target_pos.y)):
            return True
        else:
            return False

class Knight:
    POSSIBLE_MOVE = [
        [-2, -1], [-2, 1], [2, -1], [2, 1],
        [-1, -2], [-1, 2], [1, -2], [1, 2],
    ]

    def __str__(self):
        return "Knig"

    def can_move(self, start_pos, target_pos, obsctructed, is_killing, is_backward):
        for inc_x, inc_y in self.POSSIBLE_MOVE:
            if(start_pos.x + inc_x == target_pos.x and
                    start_pos.y + inc_y == target_pos.y):
                return True
        return False

class Bishop:
    def __str__(self):
        return "Bish"

    def can_move(self, start_pos, target_pos, obsctructed, is_killing, is_backward):
        if obsctructed:
            return False
        if(abs(start_pos.x - target_pos.x) == abs(start_pos.y - target_pos.y) and
                (start_pos.x != target_pos.x and start_pos.y != target_pos.y)):
            return True
        else:
            return False

class Queen:
    def __str__(self):
        return "Quee"

    def can_move(self, start_pos, target_pos, obsctructed, is_killing, is_backward):
        if obsctructed:
            return False
        if((start_pos.x == target_pos.x and start_pos.y != target_pos.y) or
                (start_pos.x != target_pos.x and start_pos.y == target_pos.y)):
            return True
        elif(abs(start_pos.x - target_pos.x) == abs(start_pos.y - target_pos.y) and
                (start_pos.x != target_pos.x and start_pos.y != target_pos.y)):
            return True
        else:
            return False

class King:
    def __str__(self):
        return "King"

    def can_move(self, start_pos, target_pos, obsctructed, is_killing, is_backward):
        if obsctructed:
            return False
        if((start_pos.x == target_pos.x and 1 == abs(start_pos.y - target_pos.y)) or
                (1 == abs(start_pos.x - target_pos.x) and start_pos.y == target_pos.y)):
            return True
        elif(1 == abs(start_pos.x - target_pos.x) and
                1 == abs(start_pos.y - target_pos.y)):
            return True
        else:
            return False

class Pawn:
    def __str__(self):
        return "Pawn"

    def can_move(self, start_pos, target_pos, obsctructed, is_killing, is_backward):
        if is_backward or obsctructed:
            return False
        elif start_pos.x == target_pos.x and 1 == abs(start_pos.y - target_pos.y):
            return True
        elif(1 == abs(start_pos.x - target_pos.x) and
                1 == abs(start_pos.y - target_pos.y) and is_killing):
            return True
        else:
            return False

