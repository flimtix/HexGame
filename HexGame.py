from HexBoard import HexBoard
from HexPiece import HexPiece
from HexCoordinate import HexCoordinate

class HexGame:
    """
    This is a class that represents the Hex Game Loop.
    """
    @staticmethod
    def play_game():
        """
        Starts the Hex Game Loop so that the color red can start entering. 
        """
        print("Welcome to Hex Games, color Red starts the game")
        
        board = HexBoard(3)
        current_player = HexPiece.RED
        
        is_playing = True
        while is_playing:
            print(board)

            while True:
                try:
                    coorinate = input(f"Player {current_player} Enter a coordinate (x,y):")

                    coorinates = coorinate.split(',')
                    if len(coorinates) < 2:
                        raise ValueError("Need a x and y coordinate")

                    coordinate = HexCoordinate(int(coorinates[0]), int(coorinates[1]))
                    board.place_piece(coordinate, current_player)
                    break
                except ValueError or IndexError as e:
                    print(f"Please enter a correct coordinate ({e})")

            winner_piece = board.check_winner()
            if winner_piece == HexPiece.EMPTY:
                if board.is_full():
                    print("Tie..")
                    is_playing = False
            else:
                print(f"Player {current_player} has won the game")
                is_playing = False

            current_player = HexPiece.RED if current_player == HexPiece.BLUE else HexPiece.BLUE
            

if __name__ == "__main__":
    HexGame.play_game()