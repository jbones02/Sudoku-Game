import pygame
import puzzle
import text

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

    # Draws menu screen
    def __draw_win_menu(self):
        self.__WIN.fill(LIGHT_GREEN)  # Make background to light green

        # Create text objects
        title_text = text.Text('Sudoku', 'assets/font.ttf', 60, self.__WIDTH // 2, self.__HEIGHT // 2 - 100, self.__WIN)
        author_text = text.Text('By Jaryd Bones', 'assets/font.ttf', 15, self.__WIDTH // 2, self.__HEIGHT // 2 - 50, self.__WIN)
        
        # Draw text objects
        title_text.draw()
        author_text.draw()

        pygame.display.update()  # Update window

    # Main menu game loop
    def __main_menu(self):
         while self.__in_menu:
              self.__clock.tick(self.__FRAME_RATE)
              self.__check_events_menu()
              self.__draw_win_menu()  # Update display

    # Checks for events in play screen
    def __check_events_play(self):
        for event in pygame.event.get():
             # User closes window
             if event.type == pygame.QUIT:
                  self.__playing = False

    # Draws play screen
    def __draw_win_play(self):
         pass

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
