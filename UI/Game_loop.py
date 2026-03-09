import pygame
import os
import pathlib
from utils.Piece_color import PieceColor
from utils.config import BOARD_ROWS, BOARD_COLS, BOARD_WIDTH, BOARD_HEIGHT, DIR_PATH, SQUARE_SIZE, OFFSET
from utils.PieceManagement import PieceLoader
from ChessBoard.Chessboard import Chessboard
from Players.Generic_player import Player1, Player2
from utils.Player_type import PlayerType
 
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
        self.dragging = False
        self.selected_piece = None

        self.WINDOW_SIZE = 1080
        self.BOARD_SIZE = BOARD_WIDTH

        self.offset_x = (self.WINDOW_SIZE - BOARD_WIDTH) // 2
        self.offset_y = (self.WINDOW_SIZE - BOARD_HEIGHT) // 2

        self.lower_offset_y = (self.offset_y * BOARD_HEIGHT)

        self.piece_manager = PieceLoader(DIR_PATH, SQUARE_SIZE)
        self.chessboard = Chessboard()

        self.rec_size = SQUARE_SIZE
        self.flags = pygame.SCALED
        self.screen = pygame.display.set_mode((self.WINDOW_SIZE, self.WINDOW_SIZE), self.flags)
        self.clock = pygame.time.Clock()
        self.running = True

        self.board_surface = pygame.Surface((self.BOARD_SIZE, self.BOARD_SIZE))
        self.board_surface.fill((200, 200, 200))

        self.p1 = Player1(PieceColor.WHITE, PlayerType.HUMAN)
        self.p2 = Player2(PieceColor.BLACK, PlayerType.HUMAN)

        self.check_x = 0
        self.check_y = 0

        self.current_turn = self.p1
        self.next_turn = self.p2

    def events(self):
        for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    self.running = False
                elif event.type == pygame.MOUSEBUTTONDOWN:
                    self.mouse_down(event)
                elif event.type == pygame.MOUSEMOTION:
                    if self.dragging:
                        self.selected_piece.rect.center = event.pos #type: ignore
                        
                elif event.type == pygame.MOUSEBUTTONUP:
                    self.mouse_up(event)
                    
    def mouse_down(self, event):
        mouse_x, mouse_y = event.pos 
        row, col = self.get_matrix_coord(mouse_x, mouse_y)
        
        if 0 <= row < 8 and 0 <= col < 8:
            piece = self.chessboard.board[row][col]
            if piece is not None and self.current_turn.player_color == piece.p_color:
                self.selected_piece = piece
                self.dragging = True
                self.original_position = (row, col)
                self.check_x = row
                self.check_y = col

                self.selected_piece.rect.topleft = self.get_screen_coord(row, col)
                
                self.chessboard.board[row][col] = None
            else: 
                self.selected_piece = None


    def mouse_up(self, event):
        if not self.dragging or self.selected_piece is None:
            return

        mx, my = event.pos
        new_row, new_col = self.get_matrix_coord(mx, my)

        if self.check_x == new_row and self.check_y == new_col:
            self.chessboard.board[self.check_x][self.check_y] = self.selected_piece
            self.selected_piece.rect.topleft = self.get_screen_coord(self.check_x, self.check_y)
            
        elif 0 <= new_row < 8 and 0 <= new_col < 8:
            self.chessboard.board[new_row][new_col] = self.selected_piece
            new_pos = self.get_screen_coord(new_row, new_col)
            self.selected_piece.rect.topleft = new_pos
            self.selected_piece.pos_x, self.selected_piece.pos_y = new_row, new_col
            self.current_turn, self.next_turn = self.next_turn, self.current_turn

        else:
            r, c = self.original_position
            self.chessboard.board[r][c] = self.selected_piece
            self.selected_piece.rect.topleft = self.get_screen_coord(r, c)

        self.dragging = False
        print(self.selected_piece.__repr__())

    def run(self):
        while self.running:
            self.events()
                        
            self.screen.fill((50, 50, 50)) 
            
            pygame.font.init()
            font = pygame.font.SysFont(None, 40)
            upper_side = (self.WINDOW_SIZE // 2, self.offset_y // 2)
            lower_side = (self.WINDOW_SIZE // 2, (self.offset_y + BOARD_HEIGHT) + (self.offset_y // 2))
            self.draw_centered_text("Whites", font, (255, 255, 255), upper_side)
            self.draw_centered_text("Blacks", font, (255, 255, 255), lower_side)

            self.draw_chessboard()
            self.draw_pieces()

            self.screen.blit(self.board_surface, (self.offset_x, self.offset_y))
            if self.dragging and self.selected_piece is not None:
                self.screen.blit(self.selected_piece.image, self.selected_piece.rect)
            pygame.display.flip()
            self.clock.tick(60)

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
        if self.dragging and self.selected_piece is not None:
            self.screen.blit(self.selected_piece.image, self.selected_piece.rect)

    def get_recsize(self):
        return self.rec_size
    
    def get_screen_coord(self, row, col):
        x = self.offset_x + (col * SQUARE_SIZE)
        y = self.offset_y + (row * SQUARE_SIZE)
        return (x, y)
    
    def get_matrix_coord(self, x, y):
        col = (x - self.offset_x) // SQUARE_SIZE
        row = (y - self.offset_y) // SQUARE_SIZE
        return row, col
    
    def draw_centered_text(self, text, font, color, center_point):
        surface = font.render(text, True, color)
        rect = surface.get_rect(center=center_point)
        self.screen.blit(surface, rect)

    def draw_highlights(self, moves):
        if self.selected_piece:
            for row, col in moves:
                overlay = pygame.Surface((SQUARE_SIZE, SQUARE_SIZE), pygame.SRCALPHA)
                pygame.draw.circle(overlay, (0, 255, 0, 100), (SQUARE_SIZE//2, SQUARE_SIZE//2), SQUARE_SIZE//4)

                pos = (col * SQUARE_SIZE, row * SQUARE_SIZE)
                self.board_surface.blit(overlay, pos)