#!/usr/bin/env python

# Liste des directions possible.
directions = {
    'HAUT': [-1, 0],
    'DROITE': [0, 1],
    'BAS': [1, 0],
    'GAUCHE': [0, -1],
}


# tourner prend une direction en paramètre et retourne une direction
# de 90° vers la droite ou la gauche.
def tourner(dir_actuel, droite):
    dir_actuel = dir_actuel.copy()

    # On inverse le signe si necessaire
    i = int(not droite)
    if not dir_actuel[i] == 0:
        dir_actuel[i] *= -1

    # On inverse l'index Y et X
    x = dir_actuel[0]
    y = dir_actuel[1]

    return [y, x]


# avance prend une position et une direction et avance une fois
# dans la direction
def avancer(position, direction):
    y = position[0] + direction[0]
    x = position[1] + direction[1]
    return [y, x]