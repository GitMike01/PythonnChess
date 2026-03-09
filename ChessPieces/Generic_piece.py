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
            return f"PN"
        elif self.__class__.__name__ == "RookPiece":
            return f"RK"
        elif self.__class__.__name__ == "KnightPiece":
            return f"KT"
        elif self.__class__.__name__ == "BishopPiece":
            return f"BP"
        elif self.__class__.__name__ == "KingPiece":
            return f"KG"
        elif self.__class__.__name__ == "QueenPiece":
            return f"QN"