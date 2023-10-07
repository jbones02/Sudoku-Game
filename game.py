import pygame
import puzzle
import requests
import text
import button
import util
import sys

class Game:
    def __init__(self):
        # Setup game
        pygame.init()
        self.__WIDTH = 600
        self.__HEIGHT = 600
        self.__PUZZLE_HEIGHT = 450
        self.__PUZZLE_WIDTH = 450
        self.__FRAME_RATE = 60
        self.__in_menu = False
        self.__playing = False
        self.__clock = pygame.time.Clock()
        self.__WIN = pygame.display.set_mode((self.__WIDTH, self.__HEIGHT))
        pygame.display.set_caption("Sudoku")
        self.__MOUSE_POS = None

        # Setup menu screen
        self.__TITLE_TEXT = text.Text('Sudoku', 'assets/font.ttf', 60, self.__WIDTH // 2, self.__HEIGHT // 2 - 100, self.__WIN)
        self.__AUTHOR_TEXT = text.Text('By Jaryd Bones', 'assets/font.ttf', 15, self.__WIDTH // 2, self.__HEIGHT // 2 - 60, self.__WIN)
        self.__start_btn = button.Button('Start', 'assets/font.ttf', 30, util.WHITE, util.BLACK, self.__WIDTH // 2, self.__HEIGHT // 2 + 20, self.__WIN, None, None)
        self.__quit_btn = button.Button('Quit', 'assets/font.ttf', 30, util.WHITE, util.BLACK, self.__WIDTH // 2, self.__HEIGHT // 2 + 80, self.__WIN, None, None)

        # Setup play screen
        self.__attempts_remaining = 3
        self.__attempts_remaining_txt = text.Text('ATTEMPTS REMAINING: 3', 'assets/font.ttf', 15, self.__WIDTH // 2 + 117, self.__HEIGHT // 2 - 277, self.__WIN)
        self.__unsolved_puzzle = []
        self.__notes_puzzle = []
        self.__solved_puzzle = []
        self.__puzzle_tiles = []
        self.__menu_btn = button.Button('Menu', 'assets/font.ttf', 30, util.WHITE, util.BLACK, self.__WIDTH // 2 + 180, self.__HEIGHT // 2 + 245, self.__WIN, None, None)
        self.__check_btn = button.Button('Check', 'assets/font.ttf', 30, util.WHITE, util.BLACK, self.__WIDTH // 2 , self.__HEIGHT // 2 + 245, self.__WIN, None, None)
        self.__auto_btn = button.Button('Auto', 'assets/font.ttf', 30, util.WHITE, util.BLACK, self.__WIDTH // 2 - 180, self.__HEIGHT // 2 + 245, self.__WIN, None, None)
        

    # Checks for events in menu screen
    def __check_events_menu(self):
        mouse_pos = pygame.mouse.get_pos()
        for event in pygame.event.get():
            # User closes window
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
            elif event.type == pygame.MOUSEBUTTONDOWN:  # If player clicks mouse
                if self.__start_btn.clicked(self.__MOUSE_POS):  # If player clicks start button
                    self.__in_menu = False
                elif self.__quit_btn.clicked(self.__MOUSE_POS):  # if player clicks exit button
                    pygame.quit()
                    sys.exit()

    # Draws menu screen
    def __draw_menu(self):
        self.__WIN.fill(util.GREEN)  # Make background light green

        # Draw objects
        self.__TITLE_TEXT.draw()
        self.__AUTHOR_TEXT.draw()
        self.__start_btn.draw()
        self.__quit_btn.draw()

        pygame.display.update()  # Update window

    # Main menu game loop
    def __menu(self):
        self.__in_menu = True
        while self.__in_menu:
            self.__clock.tick(self.__FRAME_RATE)  # Have 1 frame pass
            self.__MOUSE_POS = pygame.mouse.get_pos()  # Get mouse position
            self.__check_events_menu()  # Check for events
            self.__draw_menu()  # Update display
        self.__play() # Move to next screen

    # Creates buttons for each tile
    def __create_tile_bts(self):
        space_between = 0  # Stores space between each tile
        
        # Starting y for tiles
        y = 75
        # Create each button
        for i in range(9):
            cur_row = []  # Temp var to store cur row of buttons
            if i == 3 or i == 6:
                y += 60
            elif i != 0:
                y += 45
            x = 105  # Starting x for tiles
            for j in range(9):
                # Have extra space between boxes
                if j == 3 or j == 6:
                    x += 60
                elif j != 0:
                    x += 45
                if self.__unsolved_puzzle.board[i][j] == None:
                    cur_btn = button.Button('', 'assets/font.ttf', 27, util.WHITE, util.WHITE, x, y, self.__WIN, 40, 40)
                else:
                    num = str(self.__unsolved_puzzle.board[i][j])
                    cur_btn = button.Button(num, 'assets/font.ttf', 27, util.WHITE, util.WHITE, x, y, self.__WIN, 40, 40)
                print((cur_btn.X, cur_btn.Y), end = ' ')
                cur_row.append(cur_btn)
                self.__puzzle_tiles.append(cur_row)
            print()

            x = 60  # Reset x for next row

    def __setup_puzzles(self):
        # Use Dosuku API to get puzzle
        response = requests.get('https://sudoku-api.vercel.app/api/dosuku?query={newboard(limit:1){grids{value}}}')
        response_puzzle_unsolved = (response.json().get('newboard').get('grids'))[0].get('value')  # Extract puzzle from response
        response_puzzle_notes = (response.json().get('newboard').get('grids'))[0].get('value')
        response_puzzle_solved = (response.json().get('newboard').get('grids'))[0].get('value')

        self.__unsolved_puzzle = puzzle.Puzzle(response_puzzle_unsolved)  # Initialize unsolved puzzle
        self.__notes_puzzle = puzzle.Puzzle(response_puzzle_notes)  # Create copy of unsolved puzzle for notes

        # Generate solution with backtracking method
        self.__solved_puzzle = puzzle.Puzzle(response_puzzle_solved)

        # Convert zeros in puzzles to None
        self.__unsolved_puzzle.zeros_to_none()
        self.__solved_puzzle.zeros_to_none()

        self.__solved_puzzle.solve()

        # Print puzzles to terminal
        self.__unsolved_puzzle.print()
        self.__solved_puzzle.print()

    def __handle_tile_click(self):
        row = None
        col = None
        tile_clicked = False
        for i in range(9):
            print("Entering loop")
            for j in range(9):
                if (self.__puzzle_tiles[i][j]).clicked(self.__MOUSE_POS):
                    print("Mouse POS:", self.__MOUSE_POS)
                    tile_clicked = True
                    row = i
                    col = j
                    print('clicked: (', i, ', ', j, ')')
                    break
                    #print((i,j))
        # If tile was clicked draw a green box around it
        if tile_clicked == True:
            cur_btn = []
            cur_btn_X = self.__puzzle_tiles[row][col].X
            cur_btn_Y = self.__puzzle_tiles[row][col].Y
            print("board: ", self.__unsolved_puzzle.board[i][j])
            print(self.__unsolved_puzzle.board)
            if self.__unsolved_puzzle.board[row][col] == None:
                cur_btn = button.Button('', 'assets/font.ttf', 27, util.WHITE, util.BLUE, cur_btn_X, cur_btn_Y, self.__WIN, 40, 40)
            else:
                num = self.__unsolved_puzzle.board[row][col]
                print("num: ", num)
                cur_btn = button.Button(str(num), 'assets/font.ttf', 27, util.WHITE, util.BLUE, cur_btn_X, cur_btn_Y, self.__WIN, 40, 40)
            self.__puzzle_tiles[row][col] = cur_btn
            # TODO CHANGE NOTES PUZZLE
            #self.__puzzle_tiles[row][col].draw()  # Draw selected button
            #pygame.display.update()  # Update window


    # Checks for events in play screen
    def __check_events_play(self):
        for event in pygame.event.get():
            # User closes window
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
            elif event.type == pygame.MOUSEBUTTONDOWN:  # If player clicks mouse
                if self.__menu_btn.clicked(self.__MOUSE_POS):  # If player clicks menu button
                    self.__playing = False
                elif self.__quit_btn.clicked(self.__MOUSE_POS):  # If player clicks check button
                    pass
                elif self.__auto_btn.clicked(self.__MOUSE_POS):  # If player clicks auto button
                    pass
                self.__handle_tile_click()

    # Draws play screen
    def __draw_play(self):
        self.__WIN.fill(util.GREEN)  # Make background light green

        # Attempts remaining text
        self.__attempts_remaining_txt.draw()

        # Puzzle Boarder
        puzzle_boarder = pygame.Rect(0, 0, self.__PUZZLE_WIDTH, self.__PUZZLE_HEIGHT)
        puzzle_boarder.center = (self.__WIDTH // 2, self.__HEIGHT // 2 - 30)
        pygame.draw.rect(self.__WIN, util.BLACK, puzzle_boarder)

        # Puzzle tiles
        for row in self.__puzzle_tiles:
            for tile in row:
                tile.draw()

        # Buttons
        self.__check_btn.draw()
        self.__auto_btn.draw()
        self.__menu_btn.draw()

        pygame.display.update()  # Update window

    # Play game loop
    def __play(self):
        self.__playing = True
        self.__attempts_remaining = 3  # Reset attempts remaining

        # Setup unsolved and solved puzzles
        self.__setup_puzzles()

        # Create puzzle tile buttons
        self.__create_tile_bts()

        while self.__playing:
            self.__clock.tick(self.__FRAME_RATE)
            self.__draw_play()  # Update display
            self.__MOUSE_POS = pygame.mouse.get_pos()  # Get mouse position
            self.__check_events_play()  # Check for events
            self.__draw_play()  # Update display
        
        # Reset puzzle
        self.__attempts_remaining = 3
        self.__attempts_remaining_txt = text.Text('ATTEMPTS REMAINING: 3', 'assets/font.ttf', 15, self.__WIDTH // 2 + 117, self.__HEIGHT // 2 - 277, self.__WIN)
        self.__unsolved_puzzle = []
        self.__notes_puzzle = []
        self.__solved_puzzle = []
        self.__puzzle_tiles = []
        self.__menu()  # Move to next screen
        

    # Starts game
    def run(self):
        self.__menu()
