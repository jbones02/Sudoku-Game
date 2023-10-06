import pygame
import boardered_text
import rgb

class Button(boardered_text.Boarded_text):
    def __init__(self, text_input, font_file, size, color, x, y, WIN):
        self.__font = pygame.font.Font(font_file, size)
        self.__text_input = text_input
        self.__text = self.__font.render(self.__text_input, True, rgb.BLACK, color)
        self.__x = x
        self.__y = y
        self.__WIN = WIN
        self.__text_rect = self.__text.get_rect()
        self.__text_rect.center = (self.__x, self.__y)

        # Button dimensions
        self.__width = len(range(self.__text_rect.left, self.__text_rect.right)) + 20
        self.__height = len(range(self.__text_rect.top, self.__text_rect.bottom)) + 20
        self.__inner_rect = pygame.Rect(0, 0, self.__width - 10, self.__height - 10)
        self.__inner_rect.center = (self.__x, self.__y)
        self.__boarder_rect = pygame.Rect(0, 0, self.__width, self.__height)
        self.__boarder_rect.center = (self.__x, self.__y)

    def draw(self):
        pygame.draw.rect(self.__WIN, rgb.BLACK, self.__boarder_rect)
        pygame.draw.rect(self.__WIN, rgb.WHITE, self.__inner_rect)
        self.__WIN.blit(self.__text, self.__text_rect)

    # Checks if button was clicked
    def clicked(self, click_pos):
        if (click_pos[0] in range(self.__boarder_rect.left, self.__boarder_rect.right)) and (click_pos[1] in range(self.__boarder_rect.top, self.__boarder_rect.bottom)):
            return True
        else:
            return False
        
    # Changes color if button is being hovered over
    def hovered(self, hover_pos):
        if (hover_pos[0] in range(self.__text_rect.left, self.__text_rect.right)) and (hover_pos[1] in range(self.__text_rect.top, self.__text_rect.bottom)):
            self.__text = self.__font.render(self.text_input, True, rgb.GREY)


    '''
    def __init__(self, text, font_file, x, y, WIN):
        self.__font = pygame.font.Font(font_file, 30)
        self.__text = self.__font.render(text, True, rgb.BLACK)
        self.__x = x
        self.__y = y
        self.__WIN = WIN
        self.__text_rect = self.__text.get_rect()
        self.__text_rect.center = (self.__x, self.__y)

    def draw(self):
        self.__WIN.blit(self.__text, self.__text_rect)
    '''