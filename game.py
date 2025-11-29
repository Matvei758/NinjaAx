import pygame
from entities import PhysicsEntity




class Game:
    def __init__(self):
        pygame.init()

        self.window_width = 640
        self.window_height = 480

        self.WINDOW = pygame.display.set_mode(
            [self.window_width, self.window_height]
        )
        pygame.display.set_caption('NinjAx')

        self.running = True
        self.FPS = 60
        self.clock = pygame.time.Clock()

        self.assets = {
            'player': pygame.image.load('bin/images/entities/player.png')
        }

        self.player = PhysicsEntity(self, 'player', [50, 50], [8, 15])


        self.img = pygame.image.load('bin/images/clouds/cloud_1.png')
        self.img.set_colorkey([0, 0, 0])
        self.img_pos = [345, 200]
        self.movement = [False, False]

        self.collision_area = pygame.Rect(160, 100, 200, 25)

    def run(self):
        while self.running:

            self.WINDOW.fill([183, 229, 247])

            self.player.update([self.movement[1] - self.movement[0], 0])
            self.player.render(self.WINDOW)


            cloud_rect = pygame.Rect(self.img_pos[0], self.img_pos[1], self.img.get_width(), self.img.get_height())

            if cloud_rect.colliderect(self.collision_area):
                pygame.draw.rect(self.WINDOW, [237, 237, 37], self.collision_area)
            else:
                pygame.draw.rect(self.WINDOW, [37, 37, 37], self.collision_area)


            #pygame.draw.rect(self.WINDOW, [237, 37, 237], cloud_rect)



            self.WINDOW.blit(self.img, self.img_pos)


            #self.img_pos[1] += self.movement[1] - self.movement[0]
            self.img_pos[1] +=  (self.movement[1] - self.movement[0])




            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    self.running = False

                if event.type == pygame.KEYDOWN:

                    if event.key == pygame.K_UP:
                        self.movement[0] = True

                    if event.key == pygame.K_DOWN:
                        self.movement[1] = True

                    if event.key == pygame.K_ESCAPE:
                        self.running = False


                if event.type == pygame.KEYUP:

                    if event.key == pygame.K_UP:
                        self.movement[0] = False

                    if event.key == pygame.K_DOWN:
                        self.movement[1] = False

            pygame.display.update()
            self.clock.tick(self.FPS)

game = Game()

game.run()
pygame.quit()



