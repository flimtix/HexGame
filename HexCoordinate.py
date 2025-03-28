class HexCoordinate:
    """
    This is a class that represents a coordinate in a Hex Game.
    """
    def __init__(self, x: int, y: int):
        self.x = x
        self.y = y

    def getX(self) -> int:
        return self.x
    
    def getY(self) -> int:
        return self.y
    
    def __eq__(self, value):
        if not isinstance(value, HexCoordinate):
            raise TypeError(f"Cant compare coordinate with type {type(value)}")
        return self.getX() == value.getX() and self.getY() == value.getY()
    
    def __hash__(self):
        return hash((self.getX(), self.getY()))