import pygame

class Text:
    def __init__(self, text, font_file, size, x, y, WIN):
        self.__font = pygame.font.Font(font_file, size)
        self.__BLACK = (0, 0, 0)
        self.__text = self.__font.render(text, True, self.__BLACK)
        self.__x = x
        self.__y = y
        self.__WIN = WIN
        self.__text_rect = self.__text.get_rect()

    def draw(self):
        self.__text_rect.center = (self.__x, self.__y)
        self.__WIN.blit(self.__text, self.__text_rect)
    