import time
import os
import sys


def loadcsv(filename):
    if not os.path.exists(filename):
        return None, f"Le fichier \"{filename}\" n'existe pas."

    if not os.path.isfile(filename):
        return None, f"Le chemin \"{filename}\" mène vers un répertoire."

    if not filename.lower().endswith(".csv"):
        return None, f"Le fichier \"{filename}\" n'a pas une extension CSV."

    return opencsv(filename), None


def opencsv(filename):
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
