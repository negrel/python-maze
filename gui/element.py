class Element:
    def __init__(self, x, y, width, height):
        self.x = x
        self.y = y
        self.width = width
        self.height = height

    def draw(self, surface):
        raise Exception("Element.draw doit être réecrit")

    def get_origin_pos(self):
        return (self.x, self.y)

    def get_pos(self):
        return ((self.x - self.width / 2), (self.y - self.height / 2))

    def get_size(self):
        return (self.width, self.height)

    def get_width(self):
        return self.width

    def get_height(self):
        return self.height

    def moveby(self, x_offset, y_offset):
        self.x += x_offset
        self.y += y_offset

    def move(self, x, y):
        self.x = x
        self.y = y

    def on_quit(self, event):
        pass

    def on_active(self, event):
        pass

    def on_key_down(self, event):
        pass

    def on_key_up(self, event):
        pass

    def on_mouse_motion(self, event):
        pass

    def on_mouse_button_up(self, event):
        pass

    def on_mouse_button_down(self, event):
        pass

    def on_video_expose(self, event):
        pass

    def on_video_resize(self, event):
        pass
