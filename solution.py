from deplacement import directions
import parse

PasSortieErr = "Vous n'êtes pas sorti du labyrinthe. (ctrl-D pour quitter)"

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


MurErreur = "Vous essayer de passer à travers un mur."

# Verifie que la liste d'ordre mène a la sortie
def __verifie_list(grille, position, direction, ordres):
    for i, ordre in enumerate(ordres):
        position, direction, err = parse.ordre(position, direction, ordre)

        if not err == None:
            return (None, err)

        y, x = position
        # On vérifie si le minautore est rentrer dans un mur
        if not grille[y][x] == 99:
            return (None, MurErreur)

    return (position,  None)
