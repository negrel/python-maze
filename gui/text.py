import pygame

from gui.element import *

if not pygame.font.get_init():
    pygame.font.init()

DEFAULT_FONT_NAME = pygame.font.get_default_font()
DEFAULT_FONT_SIZE = 24
DEFAULT_FONT = pygame.font.SysFont(DEFAULT_FONT_NAME, DEFAULT_FONT_SIZE)


class Text(Element):
    def __init__(self,
                 x,
                 y,
                 label,
                 font=DEFAULT_FONT,
                 color=(0, 0, 0),
                 background=None,
                 antialias=True):
        super().__init__(x, y, 0, 0)

        self.text = font.render(label, antialias, color, background)
        self.width, self.height = self.text.get_size()

    def draw(self, surface):
        surface.blit(self.text, self.get_pos())
