import pygame
import rgb

class Text:
    def __init__(self, TEXT_INPUT, FONT_FILE, SIZE, X, Y, WIN):
        self.__FONT = pygame.font.Font(FONT_FILE, SIZE)
        self.__TEXT_INPUT = TEXT_INPUT
        self.__TEXT = self.__FONT.render(self.__TEXT_INPUT, True, rgb.BLACK)
        self.__X = X
        self.__Y = Y
        self.__WIN = WIN
        self.__text_rect = self.__TEXT.get_rect()
        self.__text_rect.center = (self.__X, self.__Y)

    def draw(self):
        self.__WIN.blit(self.__TEXT, self.__text_rect)