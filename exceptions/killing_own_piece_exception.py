class KillingOwnPieceException(Exception):
    def __init__(self):
        MESSAGE = "Invalid move, can't kill own piece"
        super(KillingOwnPieceException, self).__init__(MESSAGE)

