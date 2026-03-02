from utils.Piece_color import PieceColor
from utils.Player_type import PlayerType
from collections import deque

class GenericPlayer():
    history = deque()
    def __init__(self, player_color: PieceColor, player_type: PlayerType):
        self.player_color = player_color
        self.player_type = player_type
        

class Player1(GenericPlayer):
    def __init__(self, player_color: PieceColor, player_type: PlayerType):
        super().__init__(player_color, player_type)

    def check_color(self, p_color: PieceColor):
        if self.player_color != p_color:
            return False
        else:
            return True

class Player2(GenericPlayer):
    def __init__(self, player_color: PieceColor, player_type: PlayerType):
        super().__init__(player_color, player_type)

    def check_color(self, p_color: PieceColor):
        if self.player_color != p_color:
            return False
        else:
            return True