from ChessPieces.Generic_piece import GenericPiece

class PawnPiece(GenericPiece):

    def __init__(self, pos_x, pos_y, p_color, image):
        super().__init__(pos_x, pos_y, p_color, image)
        self.id = GenericPiece.id