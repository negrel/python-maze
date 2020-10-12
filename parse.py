#!/usr/bin/env python

from deplacement import *

PasSortieErr = "Vous n'êtes pas sorti du labyrinthe. (ctrl-D pour quitter)"

# Verifie que la suite d'ordre donnée mène vers la sortie.
def verifie_solution(grille, start, end, ordres):
    # Le minautore commence a la position start: [y, x]
    position = start
    # Par defaut on pointe vers la droite
    direction = directions["DROITE"]

    position, err = parse_ordres(grille, position, direction, ordres)
    if not err == None:
        return (False, err)

    if not position == end:
        return (False, PasSortieErr)

    return (True, None)

MurErreur = "Vous essayer de passer à travers un mur."

# Parse les ordres données et renvoie la position après avoir
# suivis les ordres
def parse_ordres(grille, position, direction, ordres):
    for i, ordre in enumerate(ordres):
        position, direction, err = parse_ordre(position, direction, ordre)

        if not err == None:
            return (None, err)

        y, x = position
        # On vérifie si le minautore est rentrer dans un mur
        if not grille[y][x] == 99:
            return (None, MurErreur)

    return (position,  None)

OrdreInvalideErreur = "ordre invalide"

# 
def parse_ordre(position, direction, ordre):
    # On avance
    if ordre == "T":
        position = avancer(position, direction)
    # On tourne à gauche
    elif ordre == "G":
        direction = tourner(direction, droite=False)
    # On tourne a droite
    elif ordre == "D":
        direction = tourner(direction, droite=True)
    # Entrer non valide, on retourne une erreur
    else:
        return (None, None, OrdreInvalideErreur)

    return (position, direction, None)
