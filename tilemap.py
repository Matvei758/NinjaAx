import pygame



class Tilemap:
    def __init__(self, game, tile_size=16):
        self.game = game
        self.tile_size = tile_size

        self.tilemap = {}
        self.offgrid_tiles = []

        for i in range(10):
            key = f'{3 + i};10'
            self.tilemap[key] = {'type': 'grass', 'variant': 1, 'pos': [3 + i, 10]}

        for i in range(15):
            key = f'10;{5 + i}'
            self.tilemap[key] = {'type': 'stone', 'variant': 1, 'pos': [10, -0 + i]}

    def render(self, surf):
        for loc in self.tilemap:
            tile = self.tilemap[loc]
            tile_type = self.game.assets[tile['type']]
            tile_variant = tile_type[tile['variant']]
            tile_pos = [tile['pos'][0] * self.tile_size, tile['pos'][1] * self.tile_size]
            surf.blit(tile_variant, tile_pos)







if __name__ == '__main__':
    map_ = Tilemap(None)
    print(map_.tilemap)
    map_.render(None)
