import pygame

NEIGHBOR_OFFSET = [
    (-1, 1), (0,1), (1, 1),
    (-1, 0), (0, 0), (1, 0),
    (-1, -1), (0, -1), (1, -1)
]
PHYSICS_TILES = {'grass', 'stone'}



class Tilemap:
    def __init__(self, game, tile_size=16):
        self.game = game
        self.tile_size = tile_size

        self.tilemap = {}
        self.offgrid_tiles = []


        self.tilemap['0;0'] = {'type': 'grass', 'variant': 5, 'pos': [0, 0]}
        self.tilemap['1;1'] = {'type': 'stone', 'variant': 7, 'pos': [1, 1]}

        for i in range(10):
            key = f'{3 + i};10'
            self.tilemap[key] = {'type': 'grass', 'variant': 1, 'pos': [3 + i, 10]}

        for i in range(15):
            key = f'10;{5 + i}'
            self.tilemap[key] = {'type': 'stone', 'variant': 1, 'pos': [10, 5 + i]}

    def tiles_around(self, pos):
        tiles = []
        tile_loc = [int(pos[0] // self.tile_size), int(pos[1] // self.tile_size)]
        for offset in NEIGHBOR_OFFSET:
            check_loc = str(tile_loc[0] + offset[0]) + ';' + str(tile_loc[1] + offset[1])
            if check_loc in self.tilemap:
                collision_tile = self.tilemap[check_loc]
                tiles.append(collision_tile)

        return tiles

    def physics_rect_around(self, pos):
        rects = []
        for tile in self.tiles_around(pos):
            if tile['type'] in PHYSICS_TILES:
                pos_x = tile['pos'][0] * self.tile_size
                pos_y = tile['pos'][1] * self.tile_size
                rect = pygame.Rect(pos_x, pos_y, self.tile_size, self.tile_size)
                rects.append(rect)
        return rects



    def render(self, surf, offset):
        for loc in self.tilemap:
            tile = self.tilemap[loc]
            tile_type = self.game.assets[tile['type']]
            tile_variant = tile_type[tile['variant']]
            tile_pos = [tile['pos'][0] * self.tile_size - offset[0], tile['pos'][1] * self.tile_size - offset[1]]
            surf.blit(tile_variant, tile_pos)







if __name__ == '__main__':
    map_ = Tilemap(None)
    print(map_.tilemap)
    map_.render(None)
