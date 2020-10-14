from gui.rect import *


class Maze(Rect):
    def __init__(
            self,
            x,
            y,
            width,
            height,
            maze,
            wall=(0, 0, 0),
            path=(255, 255, 255),
    ):
        super().__init__(x, y, width, height, background=path)
        self.maze = maze
        self.WALL_COLOR = wall
        self.PATH_COLOR = path

    def draw(self, surface):
        w = self.width / len(self.maze[0])
        h = self.height / len(self.maze)
        block_size = 0

        x, y = self.get_pos()

        # On ajoute un offset a x ou y pour centrer le labyrinthe
        if w > h:
            x += (w - h) * len(self.maze[0]) / 2
            block_size = h
        elif h > w:
            y += (h - w) * len(self.maze) / 2
            block_size = w

        for i, row in enumerate(self.maze):
            for j, col in enumerate(row):
                color = self.PATH_COLOR
                if col == -1:
                    color = self.WALL_COLOR

                xx = x + j * block_size
                yy = y + i * block_size
                Rect(xx, yy, block_size, block_size, color).draw(surface)
