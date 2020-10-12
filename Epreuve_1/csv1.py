
def readcsv(filename):

    
    matrice = []
    
    with open(filename,'r') as fic:
        for i in fic:
            x = str.split(i, ',')
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
            
            if cellule == -1:
                s += mur
        
            elif cellule == 99:
                s += vide
            
        print(s)

printcsv(matrice, '\u2588' + '\u2588', '  ')
            