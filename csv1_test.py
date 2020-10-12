import csv1

matrice = csv1.readcsv('./exemple/exemple1.csv')
print(matrice)

# couleurs affichage
MUR = '\u2588\u2588'
VIDE = '  '
VERT = '\033[92m'
ROUGE = '\033[91m'
BLEU = '\033[94m'
csv1.printcsv(matrice, (4,1), VERT, ROUGE, BLEU, MUR, VIDE)