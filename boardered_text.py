import pygame
import text
import rgb

class Boarded_text(text.Text):
    def __init__(self, TEXT_INPUT, FONT_FILE, SIZE, COLOR, X, Y, WIN):
        text.Text.__init__(self, TEXT_INPUT, FONT_FILE, SIZE, X, Y, WIN)
        self.__TEXT = self.__FONT.render(self.__TEXT_INPUT, True, rgb.BLACK, COLOR)
        self.__WIDTH = len(range(self.__text_rect.left, self.__text_rect.right)) + 20
        self.__HEIGHT = len(range(self.__text_rect.top, self.__text_rect.bottom)) + 20
        self.__inner_rect = pygame.Rect(0, 0, self.__WIDTH - 10, self.__HEIGHT - 10)
        self.__inner_rect.center = (self.__X, self.__Y)
        self.__boarder_rect = pygame.Rect(0, 0, self.__WIDTH, self.__HEIGHT)
        self.__boarder_rect.center = (self.__X, self.__Y)

    def draw(self):
        pygame.draw.rect(self.__WIN, rgb.BLACK, self.__boarder_rect)
        pygame.draw.rect(self.__WIN, rgb.WHITE, self.__inner_rect)
        self.__WIN.blit(self.__TEXT, self.__text_rect)

'''
    def __init__(self, TEXT_INPUT, FONT_FILE, SIZE, HAS_BOARDER, COLOR, X, Y, WIN):
        self.__font = pygame.font.Font(FONT_FILE, SIZE)
        self.__TEXT_INPUT = TEXT_INPUT
        if HAS_BOARDER:
            self.__text = self.__font.render(self.__TEXT_INPUT, True, rgb.BLACK, COLOR)
        else:
            self.__text = self.__font.render(self.__TEXT_INPUT, True, rgb.BLACK)
        self.__HAS_BOARDER = HAS_BOARDER
        self.__X = X
        self.__Y = Y
        self.__WIN = WIN
        self.__text_rect = self.__text.get_rect()
        self.__text_rect.center = (self.__X, self.__Y)

        # Button dimensions
        if self.__HAS_BOARDER:
            self.__WIDTH = len(range(self.__text_rect.left, self.__text_rect.right)) + 20
            self.__HEIGHT = len(range(self.__text_rect.top, self.__text_rect.bottom)) + 20
            self.__inner_rect = pygame.Rect(0, 0, self.__WIDTH - 10, self.__HEIGHT - 10)
            self.__inner_rect.center = (self.__X, self.__Y)
            self.__boarder_rect = pygame.Rect(0, 0, self.__WIDTH, self.__HEIGHT)
            self.__boarder_rect.center = (self.__X, self.__Y)

    def draw(self):
        if self.__HAS_BOARDER:
            pygame.draw.rect(self.__WIN, rgb.BLACK, self.__boarder_rect)
            pygame.draw.rect(self.__WIN, rgb.WHITE, self.__inner_rect)
        self.__WIN.blit(self.__text, self.__text_rect)

    '''