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
    if droite and droite[1] == 0:
        droite[0] = -1
    elif not droite and droite[0] == 0:
        droite[1] = -1

    # On inverse l'index Y et X
    x = dir_actuel[0]
    y = dir_actuel[1]

    return [y, x]


demitour = lambda dir: tourner(tourner(dir, droite=False), droite=False)


# avance prend une position et une direction et avance une fois
# dans la direction
def avancer(position, direction):
    y = position[0] + direction[0]
    x = position[1] + direction[1]
    return [y, x]


def analyse_chemin(chemin):
    list_direction = ""

    start = chemin[0]
    position = start
    direction = directions["DROITE"]

    for case in chemin[1:]:
        # Calcule la différence entre la position précedente et la position actuelle
        # pour deteriner la direction.
        nouvelle_direction = [case[0] - position[0], case[1] - position[1]]

        # Si la nouvelle direction et égale a la direction précédente tourner à gauche
        if nouvelle_direction == tourner(direction, droite=False):
            list_direction = list_direction + "G"
        # Pareil mais à droite
        elif nouvelle_direction == tourner(direction, droite=True):
            list_direction = list_direction + "D"
        # Demi tour si cul de sac
        elif nouvelle_direction == demitour(direction):
            list_direction = list_direction + "DD"

        # Dans tout les cas on avance
        list_direction = list_direction + "T"

        # On met a jour les infos
        direction = nouvelle_direction
        position = case

    return list_direction
