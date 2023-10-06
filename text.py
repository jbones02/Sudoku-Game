import pygame
import rgb

class Text:
    def __init__(self, text_input, font_file, size, x, y, WIN):
        self.__font = pygame.font.Font(font_file, size)
        self.__text_input = text_input
        self.__text = self.__font.render(self.__text_input, True, rgb.BLACK)
        self.__x = x
        self.__y = y
        self.__WIN = WIN
        self.__text_rect = self.__text.get_rect()
        self.__text_rect.center = (self.__x, self.__y)

    def draw(self):
        self.__WIN.blit(self.__text, self.__text_rect)
    