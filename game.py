import pygame
import puzzle
import requests
import text
import button
import rgb
import sys
import pprint

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
        self.__MOUSE_POS = None

        # Create objects for menu
        self.__TITLE_TEXT = text.Text('Sudoku', 'assets/font.ttf', 60, self.__WIDTH // 2, self.__HEIGHT // 2 - 100, self.__WIN)
        self.__AUTHOR_TEXT = text.Text('By Jaryd Bones', 'assets/font.ttf', 15, self.__WIDTH // 2, self.__HEIGHT // 2 - 60, self.__WIN)
        self.__START_BTN = button.Button('Start', 'assets/font.ttf', 30, rgb.WHITE, self.__WIDTH // 2, self.__HEIGHT // 2 + 20, self.__WIN)
        self.__QUIT_BTN = button.Button('Quit', 'assets/font.ttf', 30, rgb.WHITE, self.__WIDTH // 2, self.__HEIGHT // 2 + 80, self.__WIN)

    # Checks for events in menu screen
    def __check_events_menu(self):
        for event in pygame.event.get():
            # User closes window
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
            elif event.type == pygame.MOUSEBUTTONDOWN:  # If player clicks mouse
                if self.__START_BTN.clicked(self.__MOUSE_POS):  # If player clicks start button
                    self.__in_menu = False
                elif self.__QUIT_BTN.clicked(self.__MOUSE_POS):  # if player clicks exit button
                    pygame.quit()
                    sys.exit()

    # Draws menu screen
    def __draw_win_menu(self):
        self.__WIN.fill(rgb.GREEN)  # Make background light green

        # Draw objects
        self.__TITLE_TEXT.draw()
        self.__AUTHOR_TEXT.draw()
        self.__START_BTN.draw()
        self.__QUIT_BTN.draw()

        pygame.display.update()  # Update window

    # Main menu game loop
    def __menu(self):
        self.__in_menu = True
        while self.__in_menu:
            self.__clock.tick(self.__FRAME_RATE)  # Have 1 frame pass
            self.__MOUSE_POS = pygame.mouse.get_pos()  # Get mouse position
            self.__check_events_menu()  # Check for events
            self.__draw_win_menu()  # Update display
        self.__play()

    # Checks for events in play screen
    def __check_events_play(self):
        for event in pygame.event.get():
            # User closes window
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()

    # Draws play screen
    def __draw_win_play(self):
        self.__WIN.fill(rgb.GREEN)  # Make background light green

        pygame.display.update()  # Update window

    # Play game loop
    def __play(self):
        self.__playing = True
        # Use Dosuku API to get puzzle
        response = requests.get('https://sudoku-api.vercel.app/api/dosuku?query={newboard(limit:1){grids{value}}}')
        response_puzzle = (response.json().get('newboard').get('grids'))[0].get('value')  # Extract puzzle from response
        sudoku_puzzle = puzzle.Puzzle(response_puzzle)  # Initialize puzzle object
        sudoku_puzzle.print()
        while self.__playing:
            self.__clock.tick(self.__FRAME_RATE)
            self.__draw_win_play()  # Update display
            self.__check_events_play()  # Check for events
            self.__draw_win_play()  # Update display

    # Starts game
    def run(self):
        self.__menu()
