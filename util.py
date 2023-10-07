import pygame

WHITE = (255, 255, 255)
BLACK = (0, 0, 0)
GREY = (96, 96, 96)
GREEN = (197, 255, 188)
BLUE = (0, 0, 255)
LIGHT_GREEN = (223, 255, 218)

def is_key(input):
    if input == pygame.K_1 or pygame.K_2 or pygame.K_3 or pygame.K_4 or pygame.K_5 or pygame.K_6 or pygame.K_7 or pygame.K_8 or pygame.K_9:
        return True
    else:
        return False