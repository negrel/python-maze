#!/usr/bin/env python3

import time
import pygame

import utils
import resolveur

WINDOW_WIDTH = 800
WINDOW_HEIGHT = 600

WALL = (0, 0, 0)
BACKGROUND = (255, 255, 255)
MINAUTORE = (70, 0, 72)

SQUARE_SIZE = 25
SQUARE = pygame.Rect(0, 0, SQUARE_SIZE, SQUARE_SIZE)

# Initialisation de la bibliothèque pygame
pygame.init()

# Créer un fenêtre
game_window = pygame.display.set_mode((WINDOW_WIDTH, WINDOW_HEIGHT), pygame.HWSURFACE | pygame.DOUBLEBUF)

# Titre de la fenêtre
pygame.display.set_caption("maze.py")

def start(grille, chemin, sleep_time=0.1):
    chemin.append(chemin[len(chemin)-1])


    # On initialise l'écran avec un fond blanc
    game_window.fill(BACKGROUND)
    # On affiche le labyrinthe
    draw_maze(grille)

    game_running = True
    while game_running:
        # On boucle à travers tout les évenements
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                game_running = False
            if event.type == pygame.VIDEORESIZE:
                WINDOW_WIDTH, WINDOW_HEIGHT = event.size

        # Mise des éléments à l'écran
        if not len(chemin) == 1:
            update_frame(grille, chemin[0], chemin[1])
            chemin = chemin[1:]

        # Met à jour l'écran
        pygame.display.update()

    pygame.quit()

def draw_maze(grille):
    for i, ligne in enumerate(grille):
        for j, colonne in enumerate(ligne):
            color = BACKGROUND

            if colonne == -1:
                color = WALL

            pygame.draw.rect(game_window, color, SQUARE.move(j * SQUARE_SIZE, i * SQUARE_SIZE))

def update_frame(grille, precedente_pos, actuel_pos, sleep_time=0.3):
    # On efface le minautore à la position precedente.
    y, x = precedente_pos
    pygame.draw.rect(game_window, BACKGROUND, SQUARE.move((x * SQUARE_SIZE, y * SQUARE_SIZE)))


    # On dessine le minautore à la position actuel.
    y, x = actuel_pos
    pygame.draw.rect(game_window, MINAUTORE, SQUARE.move((x * SQUARE_SIZE, y * SQUARE_SIZE)))

    time.sleep(sleep_time)

maze = utils.opencsv("./exemple/exemple1.csv")
chemin = resolveur.plus_court_chemin(maze)

start(maze, chemin)