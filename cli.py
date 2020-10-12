#!/usr/bin/env python

from direction import *


def parse_ordres(grille, start, end, ordres):
    # Le minautore commence a la position start: [y, x]
    position = start
    # Par defaut on pointe vers la droite
    direction = directions["DROITE"]

    # On lit les ordres un par un
    for i, ordre in enumerate(ordres):
        # On avance
        if ordre == "T":
            position = avancer(position, direction)
        # On tourne à gauche
        elif ordre == "G":
            direction = tourner(direction, False)

        # On tourne a droite
        elif ordre == "D":
            direction = tourner(direction, True)

        # Entrer non valide
        else:
            raise Exception(f"L'ordre {ordre} {i} est invalide.")

        y, x = position
        # On vérifie si le minautore est rentrer dans un mur
        if not grille[y][x] == 99:
            raise Exception(
                f"L'ordre \"{ordre}\" ({i}) mène dans le mur [{y:02d}, {x:02d}]"
            )
        # On vérifie si le minautore à gagner
        elif position == end:
            print("Vous avez gagner")
            return

    print("Vous avez perdu")


def avancer(position, direction):
    x = position[0] + direction[0]
    y = position[1] + direction[1]
    return [x, y]


# Matrice d'exemple
matrix = [
    # 0,  1,  2,  3,  4,  5,  6,  7,  8,  9, 10
    [-1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1],  # 0
    [-1, 99, 99, 99, 99, -1, 99, 99, 99, 99, -1],  # 1
    [-1, 99, -1, -1, 99, -1, 99, -1, -1, 99, -1],  # 2
    [-1, 99, -1, -1, 99, 99, 99, -1, -1, 99, -1],  # 3
    [-1, 99, -1, -1, -1, -1, -1, -1, -1, 99, -1],  # 4
    [-1, 99, -1, 99, 99, 99, 99, 99, -1, 99, -1],  # 5
    [-1, 99, -1, 99, -1, -1, -1, 99, -1, 99, -1],  # 6
    [-1, 99, -1, 99, 99, 99, 99, 99, -1, 99, -1],  # 7
    [-1, 99, -1, 99, -1, 99, -1, -1, -1, 99, -1],  # 8
    [-1, 99, -1, 99, -1, 99, -1, -1, -1, 99, -1],  # 9
    [-1, 99, -1, 99, -1, 99, -1, -1, -1, 99, -1],  # 10
    [-1, 99, -1, 99, -1, 99, 99, 99, -1, 99, -1],  # 11
    [-1, 99, -1, 99, -1, -1, -1, 99, -1, 99, -1],  # 12
    [-1, 99, 99, 99, 99, 99, -1, 99, 99, 99, -1],  # 13
    [-1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1],  # 14
]

# Position de départ du minautore
start = [1, 1]
# Position de la sortie du labyrinthe
end = [13, 9]
# Liste d'ordre pour gagner
ordres = "TTTDTTGTTGTTDTTTDTTTTTTTTTTTT"
parse_ordres(matrix, start, end, ordres)