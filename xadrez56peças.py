class Piece:
    def __init__(self, color):
        self.color = color

    def __repr__(self):
        return f"{self.color} {self.__class__.__name__}"

class Pawn(Piece):
    def __repr__(self):
        return "♟" if self.color == "black" else "♙"

class Rook(Piece):
    def __repr__(self):
        return "♜" if self.color == "black" else "♖"

class Knight(Piece):
    def __repr__(self):
        return "♞" if self.color == "black" else "♘"

class Bishop(Piece):
    def __repr__(self):
        return "♝" if self.color == "black" else "♗"

class Queen(Piece):
    def __repr__(self):
        return "♛" if self.color == "black" else "♕"

class King(Piece):
    def __repr__(self):
        return "♚" if self.color == "black" else "♔"

class Board:
    def __init__(self):
        self.grid = [[None for _ in range(8)] for _ in range(8)]

    def place_piece(self, piece, row, col):
        self.grid[row][col] = piece

    def move_piece(self, start_row, start_col, end_row, end_col):
        piece = self.grid[start_row][start_col]
        if piece is None:
            print("No piece at the starting position.")
            return False
        elif end_row < 0 or end_row > 7 or end_col < 0 or end_col > 7:
            print("Destination out of bounds.")
            return False
        elif self.grid[end_row][end_col] is not None:
            print("Destination is already occupied.")
            return False
        else:
            self.grid[end_row][end_col] = piece
            self.grid[start_row][start_col] = None
            return True

    def print_board(self):
        for row in self.grid:
            print(" | ".join(str(piece) if piece is not None else " " for piece in row))
            print("-" * 31)

def setup_board(board):
    piece_order = [Rook, Knight, Bishop, Queen, King, Bishop, Knight, Rook]
    for i in range(8):
        board.place_piece(Pawn("black"), 1, i)
        board.place_piece(Pawn("white"), 6, i)
        board.place_piece(piece_order[i]("black"), 0, i)
        board.place_piece(piece_order[i]("white"), 7, i)

def main():
    board = Board()
    setup_board(board)
    board.print_board()

if __name__ == "__main__":
    main()
