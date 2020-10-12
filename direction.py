#!/usr/bin/env python

directions = {
    'HAUT': [-1, 0],
    'DROITE': [0, 1],
    'BAS': [1, 0],
    'GAUCHE': [0, -1],
}


def tourner(dir_actuel, droite):
    if droite and dir_actuel[1] == 0:
        dir_actuel[0] *= -1
    elif not droite and dir_actuel[0] == 0:
        dir_actuel[1] *= -1

    x = dir_actuel[1]
    y = dir_actuel[0]

    return [x, y]
