class InvalidCodeException(Exception):
    def __init__(self):
        MESSAGE = "Invalid code, must within a1 until h8"
        super(InvalidCodeException, self).__init__(MESSAGE)

