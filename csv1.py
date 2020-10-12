
def readcsv(filename):

    
    matrice = []
    
    with open(filename,'r') as fic:
        for i in fic:
            x = str.split(i, ',')
            y = [int(z) for z in x ]
            matrice.append(y)
            
    
    matrice = matrice[1:]
    
    return matrice
        
        

print(readcsv('Laby exemple.csv'))    

