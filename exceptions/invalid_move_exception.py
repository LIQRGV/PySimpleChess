class InvalidMoveException(Exception):
    def __init__(self):
        MESSAGE = "Invalid move"
        super(InvalidMoveException, self).__init__(MESSAGE)

