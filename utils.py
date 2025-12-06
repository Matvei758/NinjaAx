import os

import pygame

BASE_IMG_PATH = 'bin/images/'


def load_image(path):
    img = pygame.image.load(BASE_IMG_PATH + path).convert()
    img.set_colorkey([0, 0, 0])
    return img

def load_images(path):
    images = []
    for img_name in os.listdir(BASE_IMG_PATH + path):
        img = load_image(path + '/' + img_name)
        images.append(img)

    return images




if __name__ == '__main__':
    load_images('tiles/grass')