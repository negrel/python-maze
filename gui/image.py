import pygame

from gui.element import *


class Image(Element):
    def __init__(self, x, y, path):
        super().__init__(x, y, 0, 0)
        self.image = pygame.image.load(path)
        self.width, self.height = self.image.get_size()

    def draw(self, surface):
        surface.blit(self.image, self.get_pos())

    def scale(self, width, height):
        self.width, self.height = width, height
        self.image = pygame.transform.scale(self.image, (width, height))

    def flip(self, xbool=False, ybool=False):
        self.image = pygame.transform.flip(self.image, xbool, ybool)