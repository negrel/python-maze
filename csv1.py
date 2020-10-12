
def readcsv(filename):

    
    matrice = []
    
    with open(filename,'r') as fic:
        for ligne in fic:
            x = str.split(ligne, ',')
            y = [int(z) for z in x ]
            matrice.append(y)
            
    
    matrice = matrice[1:]
    
    return matrice
matrice = readcsv('Laby exemple.csv')
print(matrice)



def printcsv(matrice, mur, vide):
    
    
    for ligne in matrice:
        s = ''
        for cellule in ligne:
            s += mur if cellule == -1 else vide
            
        print(s)

printcsv(matrice, '\u2588' + '\u2588', '  ')


