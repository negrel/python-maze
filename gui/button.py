from gui.rect import *
from gui.text import *


class Button(Rect):
    def __init__(self,
                 x,
                 y,
                 width,
                 height,
                 label,
                 onclick,
                 background=(128, 128, 128),
                 border=0,
                 color=(255, 255, 255)):
        # On coupe le label si il n'y a pas assez de place
        # et on ajoute "..."
        self.text = Text(x, y, label, color=color)
        w, _ = self.text.get_size()
        if w > width:
            label = label[:-4] + "..."
            self.text = Button(x,
                               y,
                               width,
                               height,
                               label,
                               onclick,
                               background=background,
                               border=border,
                               color=color).text

        super().__init__(x, y, width, height, background, border)
        self.onclick = onclick

    def copy(self):
        left, top = self.get_origin_pos()
        return Button(left, top, self.width, self.height, self.label)

    def moveby(self, x_offset, y_offset):
        super().moveby(x_offset, y_offset)
        self.text.move(x_offset, y_offset)

    def move(self, x, y):
        super().move(x, y)
        self.text.move(x, y)

    def draw(self, surface):
        pygame.draw.rect(surface, self.background,
                         pygame.Rect(self.get_pos(), self.get_size()),
                         self.border)
        self.text.draw(surface)

    def on_mouse_button_up(self, event):
        x, y = event.pos

        left, top = self.get_pos()
        width, height = self.get_size()

        # Si le clique et dans la surface du composant
        if x > left and (left + width) > x and y > top and (top + height) > y:
            self.onclick(event)
