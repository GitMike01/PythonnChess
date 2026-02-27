import numpy as np
from ChessPieces.Generic_piece import GenericPiece
from ChessPieces.Pawn_piece import PawnPiece
from ChessPieces.Rook_piece import RookPiece
from ChessPieces.Knight_piece import KnightPiece
from ChessPieces.Bishop_piece import BishopPiece
from ChessPieces.King_piece import KingPiece
from ChessPieces.Queen_piece import QueenPiece
from utils.Piece_color import PieceColor

class Chessboard():
    def __init__(self):
        self.size = 8
        self.board = np.full((self.size, self.size), None ,dtype=object)
        self.chessboard_whites_init()
        self.chessboard_blacks_init()

    def chessboard_whites_init(self):
        row_0_layout = [
            RookPiece, KnightPiece, BishopPiece, KingPiece, QueenPiece,
            BishopPiece, KnightPiece, BishopPiece, 
        ]

        for i in range(self.size):
            self.board[1, i] = PawnPiece(1, i, PieceColor.WHITE)
            piece_class = row_0_layout[i]
            self.board[0, i] = piece_class(0, i, PieceColor.WHITE)

    def chessboard_blacks_init(self):
        row_7_layout = [
            RookPiece, KnightPiece, BishopPiece, KingPiece, QueenPiece,
            BishopPiece, KnightPiece, BishopPiece, 
        ]

        for i in range(self.size):
            self.board[6, i] = PawnPiece(6, i, PieceColor.BLACK)
            piece_class = row_7_layout[i]
            self.board[7, i] = piece_class(7, i, PieceColor.BLACK)

    def print_chessboard_status(self):
        for i in range(self.size):
            print("\n")
            for j in range(self.size):
                piece = self.board[i][j]
                print(piece.__repr__(), end=" ")