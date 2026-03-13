import numpy as np
from ChessPieces.Generic_piece import GenericPiece
from ChessPieces.Pawn_piece import PawnPiece
from ChessPieces.Rook_piece import RookPiece
from ChessPieces.Knight_piece import KnightPiece
from ChessPieces.Bishop_piece import BishopPiece
from ChessPieces.King_piece import KingPiece
from ChessPieces.Queen_piece import QueenPiece
from utils.Piece_color import PieceColor
from collections import deque
from utils.PieceManagement import PieceLoader
from utils.config import SQUARE_SIZE, DIR_PATH, BOARD_WIDTH, BOARD_COLS
from typing import Any

class Chessboard():
    def __init__(self):
        self.size = BOARD_COLS
        self.board: Any = np.full((self.size, self.size), None, dtype=object)
        self.res = PieceLoader(DIR_PATH, SQUARE_SIZE)

        self.chessboard_whites_init()
        self.chessboard_blacks_init()

    def chessboard_whites_init(self):
        row_0_layout = [
            RookPiece, KnightPiece, BishopPiece, KingPiece, QueenPiece,
            BishopPiece, KnightPiece, RookPiece, 
        ]
        row_0_types = ["rook", "knight", "bishop", "king", "queen", "bishop", "knight", "rook"]

        for i in range(self.size):
            pawn_img = self.res.sprites[PieceColor.WHITE]["pawn"]
            self.board[6, i] = PawnPiece(6, i, PieceColor.WHITE, image=pawn_img)
            piece_class = row_0_layout[i]
            piece_type = row_0_types[i]
            self.board[7, i] = piece_class(7, i, PieceColor.WHITE, image=self.res.sprites[PieceColor.WHITE][piece_type])
            
    def chessboard_blacks_init(self):
        row_7_layout = [
            RookPiece, KnightPiece, BishopPiece, KingPiece, QueenPiece,
            BishopPiece, KnightPiece, BishopPiece, 
        ]
        row_6_types = ["rook", "knight", "bishop", "king", "queen", "bishop", "knight", "rook"]

        for i in range(self.size):
            pawn_img = self.res.sprites[PieceColor.BLACK]["pawn"]
            self.board[1, i] = PawnPiece(1, i, PieceColor.BLACK, image=pawn_img)
            piece_class = row_7_layout[i]
            piece_type = row_6_types[i]
            self.board[0, i] = piece_class(0, i, PieceColor.BLACK, image=self.res.sprites[PieceColor.BLACK][piece_type])

    def print_chessboard_status(self):
        for i in range(self.size):
            print("\n")
            for j in range(self.size):
                piece = self.board[i][j]
                print(piece.__repr__(), end=" ")

    def get_size(self):
        return self.size
    
    def get_piece(self, i, j):
        piece = self.board[i, j]
        if piece is None:
            return None
        return piece