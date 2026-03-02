import pygame
import os
import pathlib
from utils.Piece_color import PieceColor
from utils.config import BOARD_ROWS, BOARD_COLS, BOARD_WIDTH, BOARD_HEIGHT, DIR_PATH, SQUARE_SIZE, OFFSET
from utils.PieceManagement import PieceLoader
from ChessBoard.Chessboard import Chessboard
 
"""
Screen -> game surface, window opened 
board_surface (pygam.Surface()) -> like a post-it, still in my hand
.blit(.Surface, coordinates) -> pasting something on that post-it
pygame.display.flip -> show the results of previus steps
"""

class WindowSetup():
    def __init__(self) -> None:
        pygame.init()
        self.pieces_list = {
            PieceColor.WHITE: [],
            PieceColor.BLACK: []
        }
        self.dir_path = "/home/tullio/Desktop/PythonChess/pieces"

        self.WINDOW_SIZE = 1080
        self.BOARD_SIZE = BOARD_WIDTH

        self.offset_x = (self.WINDOW_SIZE - BOARD_WIDTH) // 2
        self.offset_y = (self.WINDOW_SIZE - BOARD_HEIGHT) // 2

        self.piece_manager = PieceLoader(DIR_PATH, SQUARE_SIZE)
        self.chessboard = Chessboard()

        self.rec_size = SQUARE_SIZE
        self.flags = pygame.SCALED
        self.screen = pygame.display.set_mode((self.WINDOW_SIZE, self.WINDOW_SIZE), self.flags)
        self.clock = pygame.time.Clock()
        self.running = True

        self.board_surface = pygame.Surface((self.BOARD_SIZE, self.BOARD_SIZE))
        self.board_surface.fill((200, 200, 200))

    def run(self):
        while self.running:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    self.running = False
            
            self.screen.fill((50, 50, 50)) 
            self.draw_chessboard()
            self.draw_pieces()
            self.screen.blit(self.board_surface, (self.offset_x, self.offset_y))
            
            pygame.display.flip()
            self.clock.tick(30)

    def draw_chessboard(self):
        square_size = self.BOARD_SIZE // 8 
        
        colors = ["white", "black"]
        
        for i in range(BOARD_ROWS):
            for j in range(BOARD_COLS):
                pos_x = j * square_size
                pos_y = i * square_size
                
                rect = pygame.Rect(pos_x, pos_y, square_size, square_size)
                color_idx = (i + j) % 2
                pygame.draw.rect(self.board_surface, colors[color_idx], rect)

    def draw_pieces(self):
        for i in range(BOARD_ROWS):
            for j in range(BOARD_COLS):
                piece = self.chessboard.get_piece(i, j)

                if piece:
                    pos_x = (j * SQUARE_SIZE) + OFFSET
                    pos_y = (i * SQUARE_SIZE) + OFFSET

                    self.board_surface.blit(piece.image, (pos_x, pos_y))

    def get_recsize(self):
        return self.rec_size