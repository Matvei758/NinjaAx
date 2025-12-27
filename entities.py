import pygame



class PhysicsEntity:
    def __init__(self, game, e_type, pos, size):
        self.game = game
        self.type = e_type
        self.pos = list(pos)
        self.size = size

        self.velocity = [0, 0]


    def rect(self):
        return pygame.Rect(self.pos[0], self.pos[1], self.size[0], self.size[1])

    def update(self, tilemap, movement):
        frame_movement = [
            movement[0] + self.velocity[0],
            movement[1] + self.velocity[1],
        ]

        self.velocity[1] = self.velocity[1] + 0.05

        self.pos[0] += frame_movement[0]
        entity_rect = self.rect()
        pygame.draw.rect(self.game.display, [255, 30, 30], entity_rect)

        for rect in tilemap.physics_rect_around(self.pos):
            if entity_rect.colliderect(rect):
                if frame_movement[0] > 0:
                    entity_rect.right = rect.left
                if frame_movement[0] < 0:
                    entity_rect.left = rect.right

                self.pos[0] = entity_rect.x

        
        self.pos[1] += frame_movement[1]

        entity_rect = self.rect()
        pygame.draw.rect(self.game.display, [255, 30, 30], entity_rect)

        for rect in tilemap.physics_rect_around(self.pos):
            if entity_rect.colliderect(rect):
                if frame_movement[1] > 0:
                    entity_rect.bottom = rect.top
                if frame_movement[1] < 0:
                    entity_rect.top = rect.bottom

                self.pos[1] = entity_rect.y

    def render(self, surf):
        surf.blit(self.game.assets['player'], self.pos)
