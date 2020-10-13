from deplacement import *

PasSortieErr = "vous n'êtes pas sorti du labyrinthe"


# Verifie que la suite d'ordre donnée mène vers la sortie.
def verifie(grille, start, end, ordres):
    # Le minautore commence a la position start: [y, x]
    position = start
    # Par defaut on pointe vers la droite
    direction = directions["DROITE"]

    # On recupère la position après avoir vérifier
    position, err = __verifie_list(grille, position, direction, ordres)
    if not err == None:
        return (False, err)

    if not position == end:
        return (False, PasSortieErr)

    return (True, None)


MurErreur = "vous essayer de passer à travers un mur"


# Verifie que la liste d'ordre mène a la sortie
def __verifie_list(grille, position, direction, ordres):
    for i, ordre in enumerate(ordres):
        position, direction, err = __ordre(position, direction, ordre)

        if not err == None:
            return (None, err)

        y, x = position
        # On vérifie si le minautore est rentrer dans un mur
        if not grille[y][x] == 99:
            return (None, MurErreur)

    return (position, None)


OrdreInvalideErreur = "ordre invalide"


# Parse l'ordre donnée et retourne la position et la direction après avoir
# executé l'ordre
def __ordre(position, direction, ordre):
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
