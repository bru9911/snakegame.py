class Piece:
    def __init__(self, color):
        self.color = color

class Pawn(Piece):
    def __init__(self, color):
        super().__init__(color)

    def __str__(self):
        return "♟" if self.color == "black" else "♙"

class Rook(Piece):
    def __init__(self, color):
        super().__init__(color)

    def __str__(self):
        return "♜" if self.color == "black" else "♖"

class Board:
    def __init__(self):
        self.grid = [[None for _ in range(4)] for _ in range(4)]

    def place_piece(self, piece, row, col):
        self.grid[row][col] = piece

    def move_piece(self, start_row, start_col, end_row, end_col):
        piece = self.grid[start_row][start_col]
        if piece is None:
            print("No piece at the starting position.")
            return False
        elif end_row < 0 or end_row > 3 or end_col < 0 or end_col > 3:
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
            print("-------------")

# Criando as peças
black_pawn = Pawn("black")
black_rook = Rook("black")
white_pawn = Pawn("white")
white_rook = Rook("white")

# Criando o tabuleiro
board = Board()
board.place_piece(black_pawn, 1, 0)
board.place_piece(black_rook, 0, 0)
board.place_piece(white_pawn, 2, 3)
board.place_piece(white_rook, 3, 3)

# Exibindo o tabuleiro
board.print_board()

# Movendo a torre branca
board.move_piece(3, 3, 2, 3)
print("\nApós o movimento:")
board.print_board()
