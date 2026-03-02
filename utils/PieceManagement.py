import pygame 
import os
from utils.Piece_color import PieceColor
from ChessPieces.Generic_piece import GenericPiece
from ChessPieces.Pawn_piece import PawnPiece
from ChessPieces.Rook_piece import RookPiece
from ChessPieces.Knight_piece import KnightPiece
from ChessPieces.Bishop_piece import BishopPiece
from ChessPieces.King_piece import KingPiece
from ChessPieces.Queen_piece import QueenPiece
from utils.Piece_color import PieceColor
from utils.config import DIR_PATH, SQUARE_SIZE, PIECE_SIZE

class PieceLoader():
    """
    Gestisce il caricamento e la scalatura degli asset grafici dei pezzi.
    
    Analizza i nomi dei file nella directory (es. 'wp.svg', 'bk.svg'), 
    li associa alla classe logica corretta tramite una mappatura e 
    genera un dizionario di superfici Pygame scalate, pronte per il rendering.
    """
    def __init__(self, dir_path = DIR_PATH, square_size = SQUARE_SIZE) -> None:
        self.dir_path = dir_path
        self.piece_size = int(square_size * 0.85) #85% of original tile's dimension

        self.type_map = {
            'p' : 'pawn',
            'r' : 'rook',
            'n' : 'knight',
            'b' : 'bishop',
            'q' : 'queen',
            'k' : 'king'
        }

        self.sprites = {
            PieceColor.WHITE: {},
            PieceColor.BLACK: {}
        }

        self._load_images()

    def _load_images(self):
        for file in os.listdir(self.dir_path):
            filename = os.fsdecode(file)
            if filename.endswith(".svg"):
                color_char = filename[0]
                type_char = filename[1]

                color = PieceColor.WHITE if color_char == 'w' else PieceColor.BLACK

                if type_char in self.type_map:
                    piece_type = self.type_map[type_char]

                    path = os.path.join(self.dir_path, filename)
                    img_surface = pygame.image.load(path)
                    img_surface = pygame.transform.smoothscale(img_surface, (PIECE_SIZE,PIECE_SIZE))

                    self.sprites[color][piece_type] = img_surface