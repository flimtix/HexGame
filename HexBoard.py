from typing import Callable, Iterable, List
from HexPiece import HexPiece
from HexCoordinate import HexCoordinate
from colorama import Fore

class HexBoard:
    """
    This is a class that represents the board for a Hex Board Game.
    """
    def __init__(self, dimension: int):
        self.dimension = dimension
        self.board = [[HexPiece.EMPTY for _ in range(dimension)] for _ in range(dimension)]

    def place_piece(self, coordinate: HexCoordinate, piece: HexPiece):
        """
        Places a piece on the board on a specific coordinate.

        Args:
            coordinate: The coordinates where to place the piece.
            piece: The piece to place on the coordinate.

        Raises:
            ValueError: If the coordinate is occupied.
            IndexError: If the coordinate out of bound.
        """
        self._check_is_coord_occupied(coordinate)
        self.board[coordinate.getY()][coordinate.getX()] = piece

    def is_full(self) -> bool:
        """
        Checks if the board is full.

        Returns:
            True if the board is full, otherwise False.
        """
        for row in self.board:
            for column in row:
                if column == HexPiece.EMPTY:
                    return False
        return True
    
    def check_winner(self) -> HexPiece:
        """
        Checks which player won the game.

        Returns:
            The piece that won the game. If no one won yet it returns HexPiece.EMPTY.

        Raises:
            ValueError: If the coordinate is occupied.
            IndexError: If the coordinate out of bound.
        """
        def has_reached_end(color: HexPiece, to_visit: List[HexCoordinate], win_condition: Callable[[HexCoordinate], bool]):
            visited = set()
            has_won = False
            while not has_won and len(to_visit) != 0:
                piece = to_visit.pop(0)
                if win_condition(piece):
                    has_won = True
                elif piece not in visited:
                    visited.add(piece)

                    # Check the neighbors to find 
                    for neighbor in self._get_neighbors(piece):
                        if self._get_piece(neighbor) == color and neighbor not in visited:
                            to_visit.append(neighbor)
            return has_won
        
        # Start from the beggining row
        to_visit_red = [HexCoordinate(coordinate_x, 0) for coordinate_x, player in enumerate(self.board[0]) if player == HexPiece.RED]
        if has_reached_end(HexPiece.RED, to_visit_red, lambda coord: coord.getY() == self.dimension - 1):
            return HexPiece.RED
        
        # Start from the beggining column
        to_visit_blue = [HexCoordinate(0, coordinate_y) for coordinate_y, player in enumerate(self.board) if player[0] == HexPiece.BLUE]
        if has_reached_end(HexPiece.BLUE, to_visit_blue, lambda coord: coord.getX() == self.dimension - 1):
            return HexPiece.BLUE
        
        # No player won the game yet
        return HexPiece.EMPTY

    def _check_coord_in_bounds(self, coordinate: HexCoordinate):
        """
        Checks if the coordinate is out of bound

        Args:
            coordinate: The coordinate to check
        
        Raises:
            IndexError: If the coordinate out of bound.
        """
        if 0 > coordinate.getX() >= self.dimension:
            raise IndexError("The x coordinate is out of bound")
        if 0 > coordinate.getY() >= self.dimension:
            raise IndexError("The y coordinate is out of bound")

    def _check_is_coord_occupied(self, coordinate: HexCoordinate):
        """
        Checks if the coordinate is already occupied.

        Args:
            coordinate: The coordinate to check

        Raises:
            ValueError: If the coordinate is occupied.
        """
        if self._get_piece(coordinate) != HexPiece.EMPTY:
            raise ValueError("There is already a piece at that position.")
        
    def _get_piece(self, coordinate: HexCoordinate) -> HexPiece:
        """
        Gets the piece on the given coordinate.

        Args:
            coordinate: The coordinate to get the piece

        Returns:
            Returns the state of the piece in the given coordinate.

        Raises:
            IndexError: If the coordinate out of bound.
        """
        self._check_coord_in_bounds(coordinate)
        return self.board[coordinate.getY()][coordinate.getX()]

    def _get_neighbors(self, coordinate: HexCoordinate) -> Iterable[HexCoordinate]:
        """
        Gets the neighbor coordinates of a given coordinate.

        Args:
            coordinate: The coordinate to get the neighbors

        Returns:
            The neighboring coordinates.

        Raises:
            IndexError: If the coordinate out of bound.
        """
        self._check_coord_in_bounds(coordinate)

        coord_x = coordinate.getX()
        coord_y = coordinate.getY()

        for neighbor_x in range(max(0, coord_x - 1), min(self.dimension, coord_x + 2)):
            for neighbor_y in range(max(0, coord_y - 1), min(self.dimension, coord_y + 2)):
                neighbor_coord = (neighbor_x, neighbor_y)
                if neighbor_coord != (coord_x, coord_y) and neighbor_coord != (coord_x - 1, coord_y - 1) and neighbor_coord != (coord_x + 1, coord_y + 1):
                    yield HexCoordinate(neighbor_x, neighbor_y)
    
    def __str__(self):
        text = ''
        for i, row in enumerate(self.board):
            text += ' ' * i
            for column in row:
                if column == HexPiece.RED:
                    text += f"{Fore.RED}R{Fore.RESET}"
                elif column == HexPiece.BLUE:
                    text += f"{Fore.BLUE}B{Fore.RESET}"
                else:
                    text += '.'
            text += "\n"
        return text   