import os
import time

from deplacement import *
from utils import *

clear = lambda: os.system('clear')

def mur_gauche(grille):
    # On définit le point de départ et de fin du labyrinthe
    start = [1, 1]
    end = [len(grille) - 2, len(grille[0]) - 2]

    # Liste des cases par lequel ils passent
    chemin = [start]

    # Position et direction du minautore
    position = start
    direction = directions["DROITE"]

    while not position == end:
        # On essaie de tourner à gauche
        nouvelle_direction = tourner(direction, droite=False)
        y, x = avancer(position, nouvelle_direction)

        # On peut tourner a gauche
        if grille[y][x] == 99:
            direction = nouvelle_direction
            position = [y, x]
            # On ajoute la case au chemin
            chemin.append(position)
        else:
            # On tourne à droite
            direction = tourner(direction, droite=True)

    return chemin


def __mur_gauche_essai(matrix):
    # position_defini
    w = len(matrix[0])
    v = len(matrix)

    # position_initial
    x = 1
    y = 1

    direction = 0

    while not (x == w and y == v):
        if direction == 0:
            if matrix[y][x - 1] == 99:
                x = x - 1
                direction = 1

            elif matrix[y - 1][x] == 99:
                y = y - 1

            elif matrix[y][x + 1] == 99:
                x = x + 1
                direction = 3

            else:
                direction = 1

        elif direction == 1:

            if matrix[y + 1][x] == 99:
                y = y + 1
                direction = 2

            elif matrix[y][x - 1] == 99:
                x = x - 1

            elif matrix[y - 1][x] == 99:
                y = y - 1
                direction = 0

            else:
                direction = 2

        elif direction == 2:

            if matrix[y][x + 1] == 99:
                x = x + 1
                direction = 3

            elif matrix[y + 1][x] == 99:
                y = y + 1

            elif matrix[y][x - 1] == 99:
                x = x - 1
                direction = 1

            else:
                direction = 3

        elif direction == 3:

            if matrix[y - 1][x] == 99:
                y = y - 1
                direction = 0

            elif matrix[y][x + 1] == 99:
                x = x + 1

            elif matrix[y + 1][x] == 99:
                y = y + 1
                direction = 2

            else:
                direction = 0

        print(y, x, direction)


def __mur_gauche_(grille, update):
    # Définitino des variables de base
    mino_pos = [1, 1]
    mino_orientation = 0
    end = [len(grille[0]) - 2, len(grille) - 2]

    # Tant que le mino n'est pas sur la case d'arrivée
    while (mino_pos[0] != end[0] or mino_pos[1] != end[1]):
        update(grille, mino_pos)
        # On bouge le minotaure est on récupère ses nouvelles informations
        mino_pos, mino_orientation = __bougerMinotaure(grille, mino_pos,
                                                       mino_orientation)
    # On réaffiche une dernière fois pour voir le minot aure sur l'arrivée
    print_maze(grille, mino_pos)


def __bougerMinotaure(matrice, position, dir):
    orientations = [[1, 0], [0, 1], [-1, 0], [0, -1]]

    # on parcout les cases en suivant l'orientation G, T, D, GG
    for i in [-1, 0, 1, 2]:
        # On récupère les coordonnées de la case que l'on check
        offset_x = position[0] + orientations[(dir + i) % 4][0]
        offset_y = position[1] + orientations[(dir + i) % 4][1]
        # Si la case est vide, on return la nouvelle position du minotaure,
        # ainsi que sa nouvelle direction, et ses mouvements effectués
        if (matrice[offset_y][offset_x] == 99):
            return ([offset_x, offset_y], (dir + i) % 4)
        # Sinon, on continue de tourner dans la for jusqu'à trouver une case vide.

# Trouve la sortie en utilisant le chemin le plus court
def plus_court_chemin(grille):
    # On définit le point de départ et de fin du labyrinthe
    start = [1, 1]
    end = [len(grille) - 2, len(grille[0]) - 2]

    # Liste des cases par lequel ils passent
    chemin = [start]

    # Position et direction du minautore
    position = start
    direction = directions["DROITE"]

    # On trouve le chemin le plus court
    __trouver_chemin_plus_court(grille, end, end, 1)

    while not position == end:
        # On regarde le chemin le plus court parmis les chemins
        # valide.
        for y, x in __position_possible(grille, position):
            # Si le chemin est plus court
            if grille[y][x] < grille[position[0]][position[1]]:
                # On choisit ce chemin
                position = [y, x]

        chemin.append(position)

    return chemin


# Parours la grille et remplis les case avec la distance entre cette dernière et la 
# sortie.
def __trouver_chemin_plus_court(grille, actuel_pos, distance):
    # On insère la distance entre la case actuel et la sortie
    y, x = actuel_pos
    grille[y][x] = distance

    if actuel_pos == [1, 1]:
        return

    # On essaie toute les positions possible
    for prochaine_position in __position_possible(grille, actuel_pos):
        y, x = prochaine_position
        # Si la case est libre, on appelle récursivement cette fonction
        if grille[y][x] > distance:
           return __trouver_chemin_plus_court(grille, actuel_pos, prochaine_position, distance + 1)


# Retourne les prochaine position possible depuis la position donnée en paramètre.
def __position_possible(grille, position):
    pos_possible = []

    for dir in directions.values():
        y, x = avancer(position, dir)
        if not grille[y][x] == -1:
            pos_possible.append([y, x])

    return pos_possible