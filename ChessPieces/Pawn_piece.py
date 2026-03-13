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

    """
    pawn can move only Directions.UP, can also move Direction.UP_LEFT/UP_RIGHT if it can take a piece
    """
    def valid_move(self, board) -> list:
        move_coords = []
        r, c = self.pos_x, self.pos_y
        
        direction = -1 if self.p_color == PieceColor.WHITE else 1
        
        next_r = r + direction
        if 0 <= next_r < 8:
            if board[next_r][c] is None:
                move_coords.append((next_r, c))
                
                if not self.has_moved:
                    double_r = r + (2 * direction)
                    if 0 <= double_r < 8 and board[double_r][c] is None:
                        move_coords.append((double_r, c))
                        self.has_moved = True

        for dc in [-1, 1]:
            nr, nc = r + direction, c + dc
            if 0 <= nr < 8 and 0 <= nc < 8:
                target = board[nr][nc]
                if target is not None and target.p_color != self.p_color:
                    move_coords.append((nr, nc))
                
        return move_coords