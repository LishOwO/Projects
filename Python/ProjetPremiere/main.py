import sys
import pygame

class Game:
    def __init__(self):
        pygame.init()

        pygame.display.set_caption('Test game')

        self.SCREEN_WIDTH = 800
        self.SCREEN_HEIGHT = 600

        self.clock = pygame.time.Clock()

        self.screen = pygame.display.set_mode((self.SCREEN_WIDTH,self.SCREEN_HEIGHT))

        self.player = pygame.Rect((300, 250, 50, 50))

    def run(self):
        while True:
            for event in pygame.event.get():
                if event.type == pygame.quit():
                    pygame.quit()
                    sys.exit()

            pygame.display.update()
            self.clock.tick(60)

Game().run()