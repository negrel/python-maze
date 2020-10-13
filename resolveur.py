from deplacement import *
from utils import *
import os
import time
clear = lambda: os.system('clear')


def mur_gauche(grille, update):
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

        # On affiche a l'écran le labyrinthe
        update(grille, position)

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