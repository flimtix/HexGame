from enum import Enum

class HexPiece(Enum):
    """
    This is a class that represents the state of a piece.
    """
    EMPTY = 0
    RED = 1
    BLUE = 2

    def __str__(self):
        return self.name.capitalize()

