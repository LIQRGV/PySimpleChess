class PieceMoveNotAllowedException(Exception):
    def __init__(self):
        MESSAGE = "Invalid piece, must select your own piece"
        super(PieceMoveNotAllowedException, self).__init__(MESSAGE)

