import pygame
import puzzle

# Colors
WHITE = (255, 255, 255)
BLACK = (0, 0, 0)
LIGHT_GREEN = (218, 253, 179)

class Game:
    def __init__(self):
        # Setup game
        pygame.init()
        self.__WIDTH = 600
        self.__HEIGHT = 600
        self.__FRAME_RATE = 60
        self.__in_menu = False
        self.__playing = False
        self.__clock = pygame.time.Clock()
        self.__WIN = pygame.display.set_mode((self.__WIDTH, self.__HEIGHT))
        pygame.display.set_caption("Sudoku")

    # Checks for events in menu screen
    def __check_events_menu(self):
        for event in pygame.event.get():
             # User closes window
             if event.type == pygame.QUIT:
                  self.__in_menu = False

    # Checks for events in play screen
    def __check_events_play(self):
        for event in pygame.event.get():
             # User closes window
             if event.type == pygame.QUIT:
                  self.__playing = False

    # Draw title text on menu screen
    def __draw_title_text_menu(self):
        font = pygame.font.Font('assets/font.ttf', 60)
        title_text = font.render('Sudoku', True, BLACK)
        title_text_rect = title_text.get_rect()
        title_text_rect.center = (self.__WIDTH // 2, self.__HEIGHT // 2 - 100)
        self.__WIN.blit(title_text, title_text_rect)

    

    # Draws menu screen
    def __draw_win_menu(self):
        self.__WIN.fill(LIGHT_GREEN)
        self.__draw_title_text_menu()
        pygame.display.update()

    # Draws play screen
    def __draw_win_play(self):
         pass

    # Main menu game loop
    def __main_menu(self):
         while self.__in_menu:
              self.__clock.tick(self.__FRAME_RATE)
              self.__check_events_menu()
              self.__draw_win_menu()  # Update display

    # Play game loop
    def __play_game(self):
        while self.__playing:
            self.__clock.tick(self.__FRAME_RATE)
            self.__check_events_play()  # Check for events
            self.__draw_win_play()  # Update display

    # Starts game
    def start(self):
         self.__in_menu = True
         self.__main_menu()
