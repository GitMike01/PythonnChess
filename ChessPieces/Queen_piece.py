from ChessPieces.Generic_piece import GenericPiece

class QueenPiece(GenericPiece):

    def __init__(self, pos_x, pos_y, p_color):
        super().__init__(pos_x, pos_y, p_color)
        self.id = GenericPiece.id