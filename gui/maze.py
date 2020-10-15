import os
import time

from gui.rect import *
from gui.image import *
from gui.minautore import *

DEFAULT_WALL = Image(0, 0, os.path.join(".", "assets", "wall.png"))
DEFAULT_PATH = Image(0, 0, os.path.join(".", "assets", "path.png"))


class Maze(Rect):
    def __init__(
        self,
        x,
        y,
        width,
        height,
        maze,
        path,
        time_sleep=0.2,
        wall_image=DEFAULT_WALL,
        path_image=DEFAULT_PATH,
    ):
        super().__init__(x, y, width, height)
        self.maze = maze
        self.path = [path[0]] + path
        self.last_move = time.time()
        self.time_sleep = time_sleep

        self.WALL = wall_image
        self.PATH = path_image
        self.MINAUTORE = Minautore()

    def draw(self, surface):
        now = time.time()

        w = self.width / len(self.maze[0])
        h = self.height / len(self.maze)
        block_size = 0

        x, y = self.get_pos()

        # On ajoute un offset a x ou y pour centrer le labyrinthe
        if w > h:
            x += (w - h) * len(self.maze[0]) / 2
            block_size = int(h)
        elif h > w:
            y += (h - w) * len(self.maze) / 2
            block_size = int(w)

        self.WALL.scale(block_size, block_size)
        self.PATH.scale(block_size, block_size)
        self.MINAUTORE.image.scale(block_size, block_size)

        for i, row in enumerate(self.maze):
            for j, col in enumerate(row):
                xx = x + j * block_size
                yy = y + i * block_size
                block = None

                if col == -1:
                    block = self.WALL
                else:
                    block = self.PATH

                block.move(xx, yy)
                block.draw(surface)

        if now - self.last_move > self.time_sleep:
            self.last_move = now

            if not len(self.path) == 2:
                self.path = self.path[1:]

        new_pos = self.path[1]

        # On ajoute le minautore à la nouvelle position
        xx = x + new_pos[1] * block_size
        yy = y + new_pos[0] * block_size

        # print(xx, yy)

        self.MINAUTORE.move(xx, yy)
        self.MINAUTORE.draw(surface)