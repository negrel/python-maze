import pygame

pygame.font.init()
DEFAULT_FONT_NAME = pygame.font.get_default_font()
DEFAULT_FONT_SIZE = 36
DEFAULT_FONT = pygame.font.SysFont(DEFAULT_FONT_NAME, DEFAULT_FONT_SIZE)

def foreach(list, fn):
    for element in list:
        fn(element)

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

class Rect(Element, pygame.Rect):
    def __init__(self, x, y, width, height, background=(255, 255, 255), border=0):
        super().__init__(x, y, width, height)
        self.background = background
        self.border = border

    def copy(self):
        return Rect(self.x, self.y, self.width, self.height, self.background, self.border)

    def draw(self, surface):
        pygame.draw.rect(surface, self.background, self, self.border)

class Page(Rect):
    def __init__(self, name, background=(255, 255, 255)):
        super().__init__(0, 0, 0, 0, background, 0)

        self.name = name
        self.elements = []
        self.background = background

    def _dispatch_event(self, event):
        if event.type == pygame.QUIT:
            foreach(self.elements, lambda el: el.on_quit(event))
            self.quit()

        elif event.type == pygame.ACTIVEEVENT:
            foreach(self.elements, lambda el: el.on_active(event))
        elif event.type == pygame.KEYDOWN:
            foreach(self.elements, lambda el: el.on_key_down(event))
        elif event.type == pygame.KEYUP:
            foreach(self.elements, lambda el: el.on_key_up(event))
        elif event.type == pygame.MOUSEMOTION:
            foreach(self.elements, lambda el: el.on_mouse_motion(event))
        elif event.type == pygame.MOUSEBUTTONUP:
            foreach(self.elements, lambda el: el.on_mouse_button_up(event))
        elif event.type == pygame.MOUSEBUTTONDOWN:
            foreach(self.elements, lambda el: el.on_mouse_button_down(event))
        elif event.type == pygame.VIDEOEXPOSE:
            foreach(self.elements, lambda el: el.on_video_expose(event))
        elif event.type == pygame.VIDEORESIZE:
            foreach(self.elements, lambda el: el.on_video_resize(event))


    def draw(self, surface):
        foreach(self.elements, lambda el: el.draw(surface))

    def insertElement(self, index, element):
        self.elements.insert(index, element)

    def appendElement(self, element):
        self.elements.append(element)

    def removeElement(self, element):
        if element in self.elements:
            self.elements.remove(element)


class Application(Page):
    def __init__(self, name, width, height, display_mode=(pygame.HWSURFACE | pygame.DOUBLEBUF), background=(255, 255, 255)):
        super().__init__(name, background)

        self.width = width
        self.height = height

        self.display = None
        self._display_mode = display_mode
        self._running = False
        self._debug = False
        self._active_index = None
        self.elements = None
        self.page = None


    def init(self):
        if not pygame.get_init():
            pygame.init()
        if not pygame.font.get_init():
            pygame.font.init()

        self.display = pygame.display.set_mode((self.width, self.height), self._display_mode)
        self._running = True


    def debug(self, enable):
        self._debug = enable

    def quit(self):
        self._running = False
        if pygame.get_init():
            pygame.quit()
        if pygame.font.get_init():
            pygame.font.quit()

    def start(self):
        self.init()

        while self._running:
            pygame.display.set_caption(f"{self.name} - {self.page.name}")
            self.display.fill(self.background)

            # On met à jour la page
            self.page.draw(self.display)

            # On met à jour la fenêtre
            pygame.display.update()

            # On boucle à travers tout les évenements
            for event in pygame.event.get():
                if self._debug:
                    print(event)
                self.page._dispatch_event(event)

    def set_page(self, page):
        self.page = page
        page.width, page.height = self.width, self.height

class Button(Rect):
    def __init__ (self, x, y, width, height, label, onclick, background=(128, 128, 128), border=0, color=(255, 255, 255)):
        # On coupe le label si il n'y a pas assez de place
        # et on ajoute "..."
        self.text = Text(x, y, label, color=color)
        w, _ = self.text.get_size()
        if w > width:
            label = label[:-4] + "..."
            self.text = Button(x, y, width, height, label, onclick, background=background, border=border, color=color).text

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
        pygame.draw.rect(surface, self.background, pygame.Rect(self.get_pos(), self.get_size()), self.border)
        self.text.draw(surface)

    def on_mouse_button_up(self, event):
        x, y = event.pos

        left, top = self.get_pos()
        width, height = self.get_size()

        # Si le clique et dans la surface du composant
        if x > left and (left + width) > x and y > top and (top + height) > y:
            self.onclick(event)

class Text(Element):
    def __init__ (self, x, y, label, font=DEFAULT_FONT, color=(0, 0, 0), background=None, antialias=True):
        super().__init__(x, y, 0, 0)

        self.text = font.render(label, antialias, color, background)
        self.width, self.height = self.text.get_size()

    def draw(self, surface):
        surface.blit(self.text, self.get_pos())

    def split(self, start):
        pass

class Image(Element):
    def __init__ (self, x, y, path):
        super().__init__(x, y, 0, 0)
        self.image = pygame.image.load(path)
        self.width, self.height = self.image.get_size()

    def draw(self, surface):
        surface.blit(self.image, self.get_pos())

    def scale(self, width, height):
        self.width, self.height = width, height
        self.image = pygame.transform.scale(self.image, (width, height))

