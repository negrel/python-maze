import pygame

from gui.page import *

class Application(Page):
    def __init__(self,
                 name,
                 width,
                 height,
                 display_mode=(pygame.HWSURFACE | pygame.DOUBLEBUF),
                 background=(255, 255, 255)):
        super().__init__(name, background)

        self.width = width
        self.height = height

        self.display = None
        self._display_mode = display_mode
        self._running = False
        self._debug = False
        self.elements = []

    def init(self):
        if not pygame.get_init():
            pygame.init()
        if not pygame.font.get_init():
            pygame.font.init()

        self.display = pygame.display.set_mode((self.width, self.height),
                                               self._display_mode)
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
            pygame.display.set_caption(f"{self.name} - {self._page().name}")
            self.display.fill(self.background)

            # On met à jour la page
            self._page().draw(self.display)

            # On met à jour la fenêtre
            pygame.display.update()

            # On boucle à travers tout les évenements
            for event in pygame.event.get():
                if self._debug:
                    print(event)
                self._page()._dispatch_event(event)

                if event.type == pygame.QUIT:
                    self.quit()

    def push_page(self, page):
        self.elements.append(page)
        page.width, page.height = self.width, self.height

        if self._debug:
            print("/", end="")
            for p in self.elements:
                print(" ->", p.name, end="")
            print()

    def pop_page(self):
        page = self._page()
        self.elements = self.elements[:-1]

        if self._debug:
            print("/", end="")
            for p in self.elements:
                print(" ->", p.name, end="")
            print(" <-", page.name)

        if len(self.elements) == 0:
            self.quit()

        return page

    def _page(self):
        return self.elements[-1]
