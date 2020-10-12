def readcsv(filename):
    matrice = []

    with open(filename,'r') as fic:
        # On parcourt chaque ligne du CSV
        for ligne in fic:
            # Pour chaque ligne, on split le string de la cellule qu'on convertit
            # en int dans la liste m_ligne, qu'on append dans matrice
            m_ligne = [int(cell) for cell in str.split(ligne, ',')]
            matrice.append(m_ligne)
            
    # On retire la première ligne, qui correspond aux dimensions du labyrinthe
    matrice = matrice[1:]
    return matrice

matrice = readcsv('./example/example1.csv')
print(matrice)

def printcsv(matrice, mur, vide):
    # On regarde la ligne 
    for ligne in matrice:
        s = ''
        # On regarde dans la cellule 
        for cellule in ligne:
            # definit si mur ou vide
            s += mur if cellule == -1 else vide
            
        print(s)

# couleur affichage 
MUR = '\u2588\u2588'
VIDE = '  '
printcsv(matrice, MUR, VIDE)


