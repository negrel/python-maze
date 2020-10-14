#!/usr/bin/env python3

import time
import pygame
import os

import utils
import resolveur

from components import *

BLACK = (0, 0, 0)

app = Application("Maze", 1920, 1080)
width, height = app.get_size()
CENTER = (width / 2, height / 2)

app.debug(True)


# On utilise un image comme fond de fenêtre
image = Image(*CENTER, os.path.join(".", "assets", "background.jpg"))
image.scale(*app.get_size())
app.appendElement(image)

btn = Button(*CENTER, 300, 100, "Quitter", lambda event: app.quit(), background=BLACK)

app.appendElement(btn)

app.start()