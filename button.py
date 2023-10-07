import pygame
import util

class Button():
    def __init__(self, TEXT_INPUT, FONT_FILE, TEXT_SIZE, COLOR, BOARDER_COLOR, X, Y, WIN, WIDTH, HEIGHT):
        self.__font = pygame.font.Font(FONT_FILE, TEXT_SIZE)
        self.__TEXT_INPUT = TEXT_INPUT
        self.__COLOR = COLOR
        self.BOARDER_COLOR = BOARDER_COLOR
        self.__text = self.__font.render(self.__TEXT_INPUT, True, util.BLACK)
        self.X = X
        self.Y = Y
        self.__WIN = WIN
        self.__text_rect = self.__text.get_rect()
        self.__text_rect.center = (self.X, self.Y)

        # Button dimensions
        if WIDTH == None:
            self.__WIDTH = len(range(self.__text_rect.left, self.__text_rect.right)) + 20
        else:
            self.__WIDTH = WIDTH
        if HEIGHT == None: 
            self.__HEIGHT = len(range(self.__text_rect.top, self.__text_rect.bottom)) + 20
        else:
            self.__HEIGHT = HEIGHT
        self.__inner_rect = pygame.Rect(0, 0, self.__WIDTH - 10, self.__HEIGHT - 10)
        self.__inner_rect.center = (self.X, self.Y)
        self.__boarder_rect = pygame.Rect(0, 0, self.__WIDTH, self.__HEIGHT)
        self.__boarder_rect.center = (self.X, self.Y)

    # Draws button
    def draw(self):
        pygame.draw.rect(self.__WIN, self.BOARDER_COLOR, self.__boarder_rect)  # Button boarder
        pygame.draw.rect(self.__WIN, self.__COLOR, self.__inner_rect)  # Button color
        self.__WIN.blit(self.__text, self.__text_rect)  # Button text

    # Checks if button was clicked
    def clicked(self, click_pos):
        if (click_pos[0] in range(self.__boarder_rect.left, self.__boarder_rect.right)) and (click_pos[1] in range(self.__boarder_rect.top, self.__boarder_rect.bottom)):
            print("LR:", self.__boarder_rect.left, self.__boarder_rect.right)
            print('TB:', self.__boarder_rect.top, self.__boarder_rect.bottom)
            print('pos:', click_pos)
            return True
        else:
            return False
