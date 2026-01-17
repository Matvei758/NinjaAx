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

        #camera
        self.camera_scroll = [0, 0]
        


    def run(self):
        while self.running:

            self.display.fill([183, 229, 247])

            self.camera_scroll[0] += (self.player.rect().centerx - self.display.get_width() / 2 - self.camera_scroll[0]) / 25 
            self.camera_scroll[1] += (self.player.rect().centery - self.display.get_height() / 2 - self.camera_scroll[1]) / 25
            self.tilemap.render(self.display, self.camera_scroll)


            self.player.update(self.tilemap, [self.movement[1] - self.movement[0], 0])
            self.player.render(self.display, self.camera_scroll)


            







            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    self.running = False

                if event.type == pygame.KEYDOWN:

                    if event.key == pygame.K_LEFT:
                        self.movement[0] = True
                        

                    if event.key == pygame.K_RIGHT:
                        self.movement[1] = True
                    if event.key == pygame.K_UP:
                        self.player.velocity[1] = -3
                    

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











    
    



