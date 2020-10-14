import pygame

from gui.element import *


class Rect(Element, pygame.Rect):
    def __init__(self,
                 x,
                 y,
                 width,
                 height,
                 background=(255, 255, 255),
                 border=0):
        super().__init__(x, y, width, height)
        self.background = background
        self.border = border

    def copy(self):
        return Rect(self.x, self.y, self.width, self.height, self.background,
                    self.border)

    def draw(self, surface):
        pygame.draw.rect(surface, self.background, self, self.border)
