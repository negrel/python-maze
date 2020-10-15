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


def ask_open_filepath():
    tkinter.Tk().withdraw()
    return tkinter.filedialog.askopenfilename()


# Couleurs
BLACK = (0, 0, 0)
WHITE = (255, 255, 255)

# Taille standard
SQUARE_SIZE = 30
BTN_WIDTH = 150
BTN_HEIGHT = 30

# Résolution pour l'écran Alexandre
#app = Application("Maze", 1920, 1080)
# Résolution pour les écran IMERIR
app = Application("Maze", 1370, 710)
# app.debug(True)

window_width, window_height = app.get_size()
CENTER = (window_width / 2, window_height / 2)

# On utilise un image comme fond de fenêtre
image = Image(*CENTER, os.path.join(".", "assets", "background.jpg"))
image.scale(*app.get_size())

# Liste des pages
menu = None
solve = None


# Play menu
def mode_solve(algo):
    filepath = ask_open_filepath()
    if len(filepath) == 0:
        return

    play = Page("play")
    play.appendElement(image)
    play.appendElement(btn_quitter)
    play.appendElement(btn_retour)
    app.push_page(play)

    maze, err = utils.loadcsv(filepath)
    if err == None:
        chemin = algo(maze)

        play.appendElement(
            Maze(
                *CENTER,
                #Taille du maze pour ecran Imerir
                window_width / 1.5,
                window_height / 1.5,
                #Taille du maze pour ecran Alexandre
                #window_width / 2,
                #window_height / 2,
                maze,
                chemin,
                time_sleep=.5))

    else:
        play.appendElement(
            Text(*CENTER,
                 f"Une erreur c'est produite en ouvrant le ficher:",
                 color=WHITE))
        play.appendElement(
            Text(CENTER[0], CENTER[1] + BTN_HEIGHT + 10, err, color=WHITE))


# Menu
menu = Page("menu")
app.push_page(menu)

menu.appendElement(image)
menu.appendElement(
    Text(CENTER[0],
         CENTER[1] - window_height / 4,
         "MAZE",
         font=pygame.font.Font(os.path.join(".", "assets", "welingtom.ttf"),
                               DEFAULT_FONT_SIZE * 4),
         color=WHITE))

menu.appendElement(
    Button(*CENTER,
           BTN_WIDTH,
           BTN_HEIGHT,
           "Chemin le plus court",
           lambda event: mode_solve(resolveur.plus_court_chemin),
           background=WHITE,
           color=BLACK))

menu.appendElement(
    Button(CENTER[0],
           CENTER[1] + 92,
           BTN_WIDTH,
           BTN_HEIGHT,
           "Mur gauche",
           lambda event: mode_solve(resolveur.mur_gauche),
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

app.start()
