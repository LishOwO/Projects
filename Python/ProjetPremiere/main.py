import sys
import pygame


class Game:
    def __init__(self):
        pygame.init()

        pygame.display.set_caption('Test game')

        self.SCREEN_WIDTH = 800
        self.SCREEN_HEIGHT = 600

        self.MOVEMENT_VELOCITY = 5 
        
        self.clock = pygame.time.Clock()

        self.screen = pygame.display.set_mode((self.SCREEN_WIDTH,self.SCREEN_HEIGHT))

        self.player_pos = [300, 300]
        self.player = pygame.Rect((*self.player_pos, 50, 50))

        self.collision = pygame.Rect((100, 100, 50, 50))

        self.movement_x = [False, False]
        self.movement_y = [False, False]

        self.test = 0

    def test_collision(self, rectTarget, rectCollision):

        if rectTarget.right < rectCollision.left:
            return False
        if rectTarget.bottom < rectCollision.top:
            return False
        if rectTarget.left > rectCollision.right:
            return False
        if rectTarget.top > rectCollision.bottom:
            return False

        return True

    def movement(self):
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

    def wall_collision(self, rectTarget, rectCollision):
        if not self.test_collision(rectTarget, rectCollision):
            pass # do nothing
        elif rectTarget.left - self.MOVEMENT_VELOCITY <= rectCollision.right and self.movement_x[0]:
            self.movement_x[0] = False
            self.player_pos[0] = rectCollision.right
        elif rectTarget.right + self.MOVEMENT_VELOCITY >= rectCollision.left and self.movement_x[1]:
            self.movement_x[1] = False
            self.player_pos[0] = rectCollision.left - rectTarget.width
        elif rectTarget.bottom + self.MOVEMENT_VELOCITY >= rectCollision.top and self.movement_y[0]:
            self.movement_y[0] = False
            self.player_pos[1] = rectCollision.top - rectTarget.height
        elif rectTarget.top - self.MOVEMENT_VELOCITY <= rectCollision.bottom and self.movement_y[1]:
            self.movement_y[1] = False
            self.player_pos[1] = rectCollision.bottom
                

    def run(self):

        while True:
            self.screen.fill((0,0,0))

            self.movement()
            self.wall_collision(self.player,self.collision)


            print(self.movement_x, self.movement_y)

            self.player_pos[0] += (self.movement_x[1] - self.movement_x[0]) * self.MOVEMENT_VELOCITY
            self.player_pos[1] += (self.movement_y[1] - self.movement_y[0]) * self.MOVEMENT_VELOCITY

            self.player.topleft = self.player_pos


            pygame.draw.rect(self.screen, (255, 0, 0), self.player)
            pygame.draw.rect(self.screen, (0, 255, 255), self.collision)
            

           


            pygame.display.update()
            self.clock.tick(60)

Game().run()
