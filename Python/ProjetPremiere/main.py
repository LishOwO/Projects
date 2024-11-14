import pygame
pygame.init()

SCREEN_WIDTH = 800
SCREEN_HEIGHT = 600

player = pygame.Rect((300, 250, 50, 50))

screen = pygame.display.set_mode((SCREEN_WIDTH,SCREEN_HEIGHT))

run = True

while run:

    


    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            run = False
pygame.quit()

class Game:
    def __init__(self):
        self.SCREEN_WIDTH = 800
        self.SCREEN_HEIGHT = 600

        self.screen = pygame.display.set_mode((self.SCREEN_WIDTH,SCREEN_HEIGHT))

    pass

