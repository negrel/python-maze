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
    # On inverse le signe si necessaire
    i = int(not droite)
    if not dir_actuel[i] == 0:
        dir_actuel[i] *= -1
    
    # On inverse l'index Y et X
    x = dir_actuel[1]
    y = dir_actuel[0]

    return [x, y]
