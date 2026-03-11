from ChessPieces.Generic_piece import GenericPiece
from utils.Piece_color import PieceColor
from utils.Directions import Directions
import pygame

class PawnPiece(GenericPiece):
    def __init__(self, pos_x, pos_y, p_color, image):
        super().__init__(pos_x, pos_y, p_color, image)
        self.image = image
        self.rect = self.image.get_rect(topleft=(pos_x, pos_y))
        self.id = GenericPiece.id
        self.range = 1
        self.has_moved = False
        self.movement = [Directions.UP, Directions.UP_LEFT, Directions.UP_RIGHT]

    """
    pawn can move only Directions.UP, can also move Direction.UP_LEFT/UP_RIGHT if it can take a piece
    """
    def valid_move(self, board) -> list:
        move_coords = []
        
        return move_coords