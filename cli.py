#!/usr/bin/env python

ordre = "TTTTDTTGTTGTTDTTTD"

matrix = [
  [-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1],
  [-1,99,99,99,99,-1,99,99,99,99,-1],
  [-1,99,-1,-1,99,-1,99,-1,-1,99,-1],
  [-1,99,-1,-1,99,99,99,-1,-1,99,-1],
  [-1,99,-1,-1,-1,-1,-1,-1,-1,99,-1],
  [-1,99,-1,99,99,99,99,99,-1,99,-1],
  [-1,99,-1,99,-1,-1,-1,99,-1,99,-1],
  [-1,99,-1,99,99,99,99,99,-1,99,-1],
  [-1,99,-1,99,-1,99,-1,-1,-1,99,-1],
  [-1,99,-1,99,-1,99,-1,-1,-1,99,-1],
  [-1,99,-1,99,-1,99,-1,-1,-1,99,-1],
  [-1,99,-1,99,-1,99,99,99,-1,99,-1],
  [-1,99,-1,99,-1,-1,-1,99,-1,99,-1],
  [-1,99,99,99,99,99,-1,99,99,99,-1],
  [-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1],
]

def parse_ordres(grille, start, end, ordres):
  # Le minautore commence a la position start: [x, y]
  position = start
  # Par defaut on pointe vers la droite
  dir = [0, 1]

  # On lit les ordres un par un
  for i, order in enumerate(ordres):
    if order == "T":
      # TODO faire avancer le minautore
    elif order == "G":
      # TODO faire tourner le minautore de 90° vers la gauche
    elif order == "D":
      # TODO faire tourner le minautore de 90° vers la droite
    else:
      # Erreur, l'ordre entré n'existe pas.

