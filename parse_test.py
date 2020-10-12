#!/usr/bin/env python

import parse
from deplacement import directions


def TestParseOrdre():
  # On commence à une position [1, 1]
  position = [1, 1]
  direction = directions["HAUT"]

  # On tourne à GAUCHE
  nouvelle_position, nouvelle_direction, err = parse.ordre(position, direction, "D")
  # Si la position à changer ou la direction n'a PAS changer
  if nouvelle_position != position or nouvelle_direction == direction:
    raise Exception("Failed on parse \"D\"")
  
  if not nouvelle_direction == directions["DROITE"]:
    raise Exception("Failed on parse \"D\"")

  # On tourne à GAUCHE
  nouvelle_position, nouvelle_direction, err = parse.ordre(position, direction, "G")
  # Si la position à changer ou la direction n'a PAS changer
  if nouvelle_position != position or nouvelle_direction == direction:
    raise Exception("Failed on parse \"G\"")

  if not nouvelle_direction == directions["GAUCHE"]:
    raise Exception("Failed on parse \"G\"")

  # On avance
  nouvelle_position, nouvelle_direction, err = parse.ordre(position, direction, "T")
  # Si la position n'a PAS changer ou la direction a changer
  if nouvelle_position == position or nouvelle_direction != direction:
    raise Exception("Failed on parse \"T\"")

  if not nouvelle_position == [0, 1]:
    raise Exception("Failed on parse \"T\"")

TestParseOrdre()
