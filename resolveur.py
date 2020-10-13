from deplacement import *
from utils import *
import os
import time
clear = lambda: os.system('clear')


def mur_gauche(grille):
    start = [1, 1]
    end = [len(grille) - 2, len(grille[0]) - 2]

    chemin = [start]

    position = start
    direction = directions["DROITE"]

    while not position == end:
        nouvelle_direction = tourner(direction, droite=False)
        y, x = avancer(position, nouvelle_direction)

        if grille[y][x] == 99:
            direction = nouvelle_direction
            position = [y, x]
            chemin.append(position)
        else:
            direction = tourner(direction, droite=True)

        # On affiche a l'écran le labyrinthe
        time.sleep(0.1)
        clear()
        print_maze(grille, position)

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


def __mur_gauche_(grille):
    # Définitino des variables de base
    mino_pos = [1, 1]
    mino_orientation = 0
    end = [len(grille[0]) - 2, len(grille) - 2]
    moves = ''

    # Tant que le mino n'est pas sur la case d'arrivée
    while (mino_pos[0] != end[0] or mino_pos[1] != end[1]):
        # On clear la console et on affiche la labyrinthe
        clear()
        csv1.printcsv(laby, mino_pos)
        # On bouge le minotaure est on récupère ses nouvelles informations
        mino_pos, mino_orientation, m = __bougerMinotaure(
            laby, mino_pos, mino_orientation)
        # On met à jour les mouvements effectués
        moves += m
        time.sleep(0.2)
    # On réaffiche une dernière fois pour voir le minot aure sur l'arrivée
    csv1.printcsv(laby, mino_pos)
    print("Labyrinthe résolu en " + str(len(moves)) + " coups.")
    print("Liste des coups :")
    print(moves)


def __bougerMinotaure(matrice, position, dir):
    orientations = [[1, 0], [0, 1], [-1, 0], [0, -1]]
    str_orientation = ['G', 'T', 'D', 'GG']

    # on parcout les cases en suivant l'orientation G, T, D, GG
    for i in [-1, 0, 1, 2]:
        # On récupère les coordonnées de la case que l'on check
        offset_x = position[0] + orientations[(dir + i) % 4][0]
        offset_y = position[1] + orientations[(dir + i) % 4][1]
        # Si la case est vide, on return la nouvelle position du minotaure,
        # ainsi que sa nouvelle direction, et ses mouvements effectués
        if (matrice[offset_y][offset_x] == 99):
            str_move = str_orientation[i + 1] + ('T' if i != 0 else '')
            return ([offset_x, offset_y], (dir + i) % 4, str_move)
        # Sinon, on continue de tourner dans la for jusqu'à trouver une case vide.
