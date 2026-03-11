from utils.Piece_color import PieceColor
from abc import ABC, abstractmethod
from typing import List, Tuple

class GenericPiece:
    id = 0
    def __init__ (self, pos_x: int, pos_y: int, p_color: PieceColor, image=None):
        self.pos_x = pos_x
        self.pos_y = pos_y
        self.p_color = p_color
        self.image = image
        GenericPiece.id += 1
    
    @abstractmethod
    def valid_move(self, board) -> List[Tuple[int, int]]:
        pass
    
    def __str__(self) -> str:
        return f"{self.__class__.__name__}, id = {self.id}, pos_x = {self.pos_x}, pos_y = {self. pos_y}, ({self.p_color})"
    
    def __repr__(self) -> str: #type: ignore
        if self.__class__.__name__ == "PawnPiece":
            return f"WP" if self.p_color == PieceColor.WHITE else f"BP"
        elif self.__class__.__name__ == "RookPiece":
            return f"WR" if self.p_color == PieceColor.WHITE else f"BR"
        elif self.__class__.__name__ == "KnightPiece":
            return f"WK" if self.p_color == PieceColor.WHITE else f"BK"
        elif self.__class__.__name__ == "BishopPiece":
            return f"WB" if self.p_color == PieceColor.WHITE else f"BB"
        elif self.__class__.__name__ == "KingPiece":
            return f"WK" if self.p_color == PieceColor.WHITE else f"BK"
        elif self.__class__.__name__ == "QueenPiece":
            return f"WQ" if self.p_color == PieceColor.WHITE else f"BQ"