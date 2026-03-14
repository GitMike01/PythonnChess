from ChessPieces.Generic_piece import GenericPiece
from utils.Directions import Directions

class QueenPiece(GenericPiece):
    def __init__(self, pos_x, pos_y, p_color, image):
        super().__init__(pos_x, pos_y, p_color, image)
        self.image = image
        self.rect = self.image.get_rect(topleft=(pos_x, pos_y))
        self.id = GenericPiece.id
        self.directions = [Directions.UP_LEFT.value, Directions.UP_RIGHT.value,
                           Directions.DOWN_LEFT.value, Directions.DOWN_RIGHT.value,
                           Directions.UP.value, Directions.DOWN.value,
                           Directions.RIGHT.value, Directions.LEFT.value]

    def valid_move(self, board) -> list:
        moves = []
        for dr, dc in self.directions:
            new_r = dr + self.pos_x #nuova posizione in riga
            new_c = dc + self.pos_y #nuova posizione in colonna
            tmp_x = new_r
            tmp_y = new_c
            for i in range(0, 8):
                if 0 <= tmp_x < 8 and 0 <= tmp_y < 8:
                    if board[tmp_x][tmp_y] == None:
                        moves.append((tmp_x, tmp_y))
                        tmp_x += dr
                        tmp_y += dc
                    elif board[tmp_x][tmp_y] != None:
                        piece = board[tmp_x][tmp_y]
                        if piece.p_color != self.p_color:
                            moves.append((tmp_x, tmp_y))
                            print(f"{tmp_x}, {tmp_y}")
                            break
        return moves