#!/usr/bin/env python3

def readcsv(filename):
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

def printcsv(matrice, cDepart, cArrivee, position, cMinotaure, mur='\u2588\u2588', vide='  '):
    i, j = 0, 0
    for ligne in matrice:
        s = ''
        # On regarde dans la cellule 
        for cellule in ligne:
            if (i == 1 and j == 1):
                s += cDepart
                s += mur
                s += '\033[0m'
            elif (i == len(matrice[0])-2 and j == len(matrice)-2):
                s += cArrivee
                s += mur
                s += '\033[0m'
            elif (position == (i, j)):
                s += cMinotaure
                s += mur
                s += '\033[0m'
            else:
                s += mur if cellule == -1 else vide
            i += 1
        i = 0
        j += 1
        print(s)