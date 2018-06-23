from components import (
    Chess,
    PieceSide,
)

chess = Chess()

played_side = PieceSide.WHITE
while(True):
    pos_from = input("Select tile: ")
    pos_to = input("Move to: ")

    try:
        chess.move(played_side, pos_from, pos_to)

        for row in chess.position:
            print(*[info.piece_type if info is not None else None for info in row])

        if played_side == PieceSide.WHITE:
            played_side = PieceSide.BLACK
        else:
            played_side = PieceSide.WHITE
    except Exception as e:
        print(e)


