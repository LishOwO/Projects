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

        self.player_pos = [300, 300]
        self.player = pygame.Rect((*self.player_pos, 50, 50))
        self.movement_x = [False, False]
        self.movement_y = [False, False]

        self.test = 0

    def run(self):

        while True:
            self.screen.fill((0,0,0))

            self.player_pos[0] += (self.movement_x[1] - self.movement_x[0]) * 5
            self.player_pos[1] += (self.movement_y[1] - self.movement_y[0]) * 5

            self.player.topleft = self.player_pos


            pygame.draw.rect(self.screen,(255, 0, 0),self.player)

            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    pygame.quit()
                    sys.exit()
                if event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_UP:
                        self.movement_y[0] = True
                    if event.key == pygame.K_DOWN:
                        self.movement_y[1] = True
                    if event.key == pygame.K_LEFT:
                        self.movement_x[0] = True
                    if event.key == pygame.K_RIGHT:
                        self.movement_x[1] = True
                if event.type == pygame.KEYUP:
                    if event.key == pygame.K_UP:
                        self.movement_y[0] = False
                    if event.key == pygame.K_DOWN:
                        self.movement_y[1] = False
                    if event.key == pygame.K_LEFT:
                        self.movement_x[0] = False
                    if event.key == pygame.K_RIGHT:
                        self.movement_x[1] = False


            pygame.display.update()
            self.clock.tick(60)

Game().run()