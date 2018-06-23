class InvalidPieceException(Exception):
    def __init__(self):
        MESSAGE = "Invalid piece, must select occupied code"
        super(InvalidPieceException, self).__init__(MESSAGE)

