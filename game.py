import pygame
import puzzle

# Colors
WHITE = (255, 255, 255)
BLACK = (0, 0, 0)
LIGHT_GREEN = (218, 253, 179)

class Game:
    def __init__(self):
        # Setup game
        self.__WIDTH = 600
        self.__HEIGHT = 600
        self.__FRAME_RATE = 60
        self.__in_menu = True
        self.__playing = False
        self.__clock = pygame.time.Clock()
        self.__WIN = pygame.display.set_mode((self.__WIDTH, self.__HEIGHT))
        pygame.display.set_caption("Sudoku")

    def __check_events_menu(self):
        for event in pygame.event.get():
             # User closes window
             if event.type == pygame.QUIT:
                  self.__in_menu = False

    def __check_events_play(self):
        for event in pygame.event.get():
             # User closes window
             if event.type == pygame.QUIT:
                  self.__playing = False

    def __draw_win(self):
            self.__WIN.fill(LIGHT_GREEN)
            pygame.display.update()

    def __main_menu(self):
         while self.__in_menu:
              self.__draw_win()  # Update display

    def __play_game(self):
        while self.__playing:
            self.__clock.tick(self.__FRAME_RATE)
            self.__check_events()  # Check for events
            self.__draw_win()  # Update display

         