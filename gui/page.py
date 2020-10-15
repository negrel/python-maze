import pygame

from gui.rect import *


def foreach(list, fn):
    for element in list:
        fn(element)


class Page(Rect):
    def __init__(self, name, background=(255, 255, 255)):
        super().__init__(0, 0, 0, 0, background, 0)

        self.name = name
        self.background = background
        self.elements = []

    def _dispatch_event(self, event):
        if event.type == pygame.QUIT:
            foreach(self.elements, lambda el: el.on_quit(event))
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
        surface.fill(self.background)
        foreach(self.elements, lambda el: el.draw(surface))

    def insertElement(self, index, element):
        self.elements.insert(index, element)

    def appendElement(self, element):
        self.elements.append(element)

    def removeElement(self, element):
        if element in self.elements:
            self.elements.remove(element)
