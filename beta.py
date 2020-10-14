#!/usr/bin/env python3

import time
import pygame
import os

import utils
import resolveur

from gui.application import *
from gui.button import *
from gui.image import *
from gui.page import *

# Couleurs
BLACK = (0, 0, 0)
WHITE = (255, 255, 255)

# Taille standard
BTN_WIDTH = 248
BTN_HEIGHT = 56

app = Application("Maze", 1920, 1080)
# app.debug(True)

window_width, window_height = app.get_size()
CENTER = (window_width / 2, window_height / 2)

# On utilise un image comme fond de fenêtre
image = Image(*CENTER, os.path.join(".", "assets", "background.jpg"))
image.scale(*app.get_size())

# Liste des pages
menu = None
play = None
solve = None

# Menu
menu = Page("menu")
menu.appendElement(image)
app.push_page(menu)

menu.appendElement(
    Button(*CENTER,
           BTN_WIDTH,
           BTN_HEIGHT,
           "Jouer",
           lambda event: app.push_page(play),
           background=WHITE,
           color=BLACK))
menu.appendElement(
    Button(CENTER[0],
           CENTER[1] + 92,
           BTN_WIDTH,
           BTN_HEIGHT,
           "Résoudre",
           lambda event: print("Résoudre"),
           background=WHITE,
           color=BLACK))

# Bouton pour quitter l'application
btn_quitter = Button(CENTER[0] + (BTN_WIDTH + 10),
                     (window_height - window_height / 10),
                     BTN_WIDTH,
                     BTN_HEIGHT,
                     "Quitter",
                     lambda event: app.quit(),
                     background=BLACK)
menu.appendElement(btn_quitter)

btn_retour = Button(CENTER[0] - (BTN_WIDTH + 10),
                    (window_height - window_height / 10),
                    BTN_WIDTH,
                    BTN_HEIGHT,
                    "Retour",
                    lambda event: app.pop_page(),
                    background=BLACK)
menu.appendElement(btn_retour)

# Play menu
play = Page("play")
play.appendElement(image)
play.appendElement(btn_quitter)
play.appendElement(btn_retour)

app.start()