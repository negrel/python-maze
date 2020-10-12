def readcsv(filename):
    matrice = []

    with open(filename,'r') as fic:
        for ligne in fic:
            m_ligne = [int(cell) for cell in str.split(ligne, ',')]
            matrice.append(m_ligne)
            
    matrice = matrice[1:]
    return matrice

matrice = readcsv('./example/example1.csv')
print(matrice)

def printcsv(matrice, mur, vide):
    for ligne in matrice:
        s = ''
        for cellule in ligne:
            s += mur if cellule == -1 else vide
        print(s)

MUR = '\u2588\u2588'
VIDE = '  '
printcsv(matrice, MUR, VIDE)


