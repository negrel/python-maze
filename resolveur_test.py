from resolveur import *
from utils import loadcsv

grille = loadcsv("exemple/exemple1.csv")

print("ligne", len(grille), "colonne", len(grille[0]))

def print_maze(grille):
  for i in range(len(grille[0])):
    print(f"{i:2d}", end="")
  print("")
  
  for i, ligne in enumerate(grille):
    for colonne in ligne:
      if colonne == -1:
        print("\u2588\u2588", end="")
      else:
        print(f"{colonne:2d}", end="")
    print(f" {i:}")

find_short_path(grille, [len(grille) - 2, len(grille[0]) - 2], [len(grille) - 2, len(grille[0]) - 2], 1)

print_maze(grille)