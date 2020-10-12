#!/usr/bin/env python

from deplacement import *

def TestTourner():
  nom_directions = ["HAUT", "DROITE", "BAS", "GAUCHE"]


  for i, nom in enumerate(nom_directions):
    expected = directions[nom_directions[(i + 1) % 4]]
    actual = tourner(directions[nom].copy(), droite=True)

    if not expected == actual :
      raise Exception("Erreur: tourner à droite")

  for i, nom in enumerate(nom_directions):
    expected = directions[nom_directions[(i - 1) % 4]]
    actual = tourner(directions[nom].copy(), droite=False)

    if not expected == actual:
      raise Exception("Erreur: tourner à gauche")


TestTourner()