import pygame
from entities import PhysicsEntity
from utils import load_image, load_images
from tilemap import Tilemap




class Game:
    def __init__(self):
        pygame.init()

        self.window_width = 960
        self.window_height = 720

        self.WINDOW = pygame.display.set_mode(
            [self.window_width, self.window_height]
        )

        self.display = pygame.Surface([320, 240])




        self.running = True
        self.FPS = 60
        self.clock = pygame.time.Clock()

        self.assets = {
            'player': load_image('entities/player.png'),
            'grass': load_images('tiles/grass'),
            'stone': load_images('tiles/stone'),

        }

        print(self.assets['grass'])

        self.player = PhysicsEntity(self, 'player', [50, 50], [8, 15])
        self.movement = [False, False]

        self.tilemap = Tilemap(self)


    def run(self):
        while self.running:

            self.display.fill([183, 229, 247])

            self.tilemap.render(self.display)

            tiles_around = self.tilemap.physics_rect_around(self.player.pos)
            

            for rect in tiles_around:
                pygame.draw.rect(self.display, [255, 0, 0], rect)

            self.player.update(self.tilemap, [self.movement[1] - self.movement[0], 0])
            self.player.render(self.display)


            







            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    self.running = False

                if event.type == pygame.KEYDOWN:

                    if event.key == pygame.K_LEFT:
                        self.movement[0] = True

                    if event.key == pygame.K_RIGHT:
                        self.movement[1] = True

                    if event.key == pygame.K_ESCAPE:
                        self.running = False


                if event.type == pygame.KEYUP:

                    if event.key == pygame.K_LEFT:
                        self.movement[0] = False

                    if event.key == pygame.K_RIGHT:
                        self.movement[1] = False

            scaled_display = pygame.transform.scale(self.display, self.WINDOW.get_size())
            self.WINDOW.blit(scaled_display, [0, 0])
            pygame.display.set_caption(f'NinjAx [FPS: {self.clock.get_fps():.0f}]')
            pygame.display.update()
            self.clock.tick(self.FPS)

if __name__ == '__main__':
    game = Game()

    game.run()
    pygame.quit()



