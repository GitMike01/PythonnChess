from typing import List, Tuple

from ChessPieces.Generic_piece import GenericPiece

class KnightPiece(GenericPiece):

    def __init__(self, pos_x, pos_y, p_color, image):
        super().__init__(pos_x, pos_y, p_color, image)
        self.image = image
        self.rect = self.image.get_rect(topleft=(pos_x, pos_y))
        self.id = GenericPiece.id
        self.directions = [(2, 1), (2, -1), (-2, 1), (2, -1), (1, 2), (1, -2), (-1, 2), (-1, -2)]

    def valid_move(self, board) -> list:
        moves = []
        for dr, dc in self.directions:
            new_r = dr + self.pos_x #nuova posizione in riga
            new_c = dc + self.pos_y #nuova posizione in colonna
            tmp_x = new_r
            tmp_y = new_c
            iter = 1
            if 0 <= tmp_x < 8 and 0 <= tmp_y < 8:
                print(f"{tmp_x}, {tmp_y}, iter: {iter}")
                iter += 1
                if board[tmp_x][tmp_y] == None:
                    moves.append((tmp_x, tmp_y))
                elif board[tmp_x][tmp_y] != None:
                    piece = board[tmp_x][tmp_y]
                    if piece.p_color != self.p_color:
                        moves.append((tmp_x, tmp_y))
                        print(f"{tmp_x}, {tmp_y}")
                        break
        return moves