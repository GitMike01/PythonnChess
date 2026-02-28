import pygame
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

        self.flags = pygame.SCALED
        self.screen = pygame.display.set_mode((1080, 1080), self.flags)
        self.clock = pygame.time.Clock()
        self.running = True

        self.board_surface = pygame.Surface((1080, 1080))
        self.board_surface.fill((200, 200, 200))

    def run(self):
        while self.running:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    self.running = False
            
            self.screen.fill("brown")
            self.draw_chessboard()
            self.screen.blit(self.board_surface, (0,0))
            
            pygame.display.flip()
            self.clock.tick(30)
        test_rect = pygame.Rect(50, 50, 100, 100)
        pygame.draw.rect(self.board_surface, 'white', test_rect)

    def draw_chessboard(self):
        chessboard = Chessboard()
        rec_size = 135
        colors = [["white", "black", "white", "black", "white", "black", "white", "black"],
                  ["black", "white", "black", "white", "black", "white", "black", "white"]]
        for i in range(chessboard.get_size()):
            for j in range(chessboard.get_size()):
                pos_x = j*rec_size
                pos_y = i*rec_size
                rect = pygame.Rect(pos_x,pos_y,135,135)
                pygame.draw.rect(self.board_surface, colors[i%2][j], rect)
        