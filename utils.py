def print_maze(matrice,
               position,
               cDepart='\033[92m',
               cArrivee='\033[94m',
               cMinotaure='\033[91m',
               mur='\u2588\u2588',
               vide='  '):
    for i, ligne in enumerate(matrice):
        s = ''
        # On regarde dans la cellule
        for j, cellule in enumerate(ligne):
            if (i == 1 and j == 1):
                s += cDepart
                s += mur
                s += '\033[0m'
            elif (position[0] == i and position[1] == j):
                s += cMinotaure
                s += mur
                s += '\033[0m'
            elif (i == len(matrice[0]) - 2 and j == len(matrice) - 2):
                s += cArrivee
                s += mur
                s += '\033[0m'
            else:
                s += mur if cellule == -1 else vide
        print(s)


def loadcsv(filename):
    matrice = []
    with open(filename, 'r') as fic:
        # On parcourt chaque ligne du CSV
        for ligne in fic:
            # Pour chaque ligne, on split le string de la cellule qu'on convertit
            # en int dans la liste m_ligne, qu'on append dans matrice
            m_ligne = [int(cell) for cell in str.split(ligne, ',')]
            matrice.append(m_ligne)

    # On retire la première ligne, qui correspond aux dimensions du labyrinthe
    matrice = matrice[1:]
    return matrice
