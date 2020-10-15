#!/usr/bin/env python3

import time
import pygame
import os
import tkinter
import tkinter.filedialog

import utils
import resolveur
from gui.application import *
from gui.button import *
from gui.image import *
from gui.page import *
from gui.maze import *





# Couleurs
BLACK = (0, 0, 0)
WHITE = (255, 255, 255)

# Taille standard
SQUARE_SIZE = 36
BTN_WIDTH = 248
BTN_HEIGHT = 56

app = Application("Maze", 1920, 1080)
# app.debug(True)

window_width, window_height = app.get_size()
CENTER = (window_width / 2, window_height / 2)

# On utilise un image comme fond de fenêtre
image = Image(*CENTER, os.path.join(".", "assets", "galaxy-1.jpg"))
image.scale(*app.get_size())

# Liste des pages
menu = None
solve = None






