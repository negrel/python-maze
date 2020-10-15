import os

from gui.image import *

DEFAULT_MINAUTORE = Image(0, 0, os.path.join(".", "assets", "minautore.png"))


class Minautore():
    def __init__(self, image=DEFAULT_MINAUTORE):
        self.image = image
        self.left_oriented = True

    def draw(self, surface):
        self.image.draw(surface)

    def move(self, x, y):
        xx, _ = self.image.get_origin_pos()

        # Gère l'orientation de l'image
        if self.left_oriented and xx - x < 0:
            self.image.flip(xbool=True)
            self.left_oriented = False
        if not self.left_oriented and xx - x > 0:
            self.image.flip(xbool=True)
            self.left_oriented = True

        self.image.move(x, y)
