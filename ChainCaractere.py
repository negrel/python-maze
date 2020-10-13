#!/usr/bin/env python3
# -*- coding: utf-8 -*-
from deplacement import *
"""
Created on Mon Oct 12 11:42:08 2020
@author: vivien
"""
def direction(chemin):
    list_direction = ""

    start = chemin[0]
    position = start
    direction = directions["DROITE"]

    for case in chemin[1:]:
        # Calcule la différence entre la position précedente et la position actuelle
        # pour deteriner la direction.
        nouvelle_direction = [case[0] - position[0], case[1] - position[1]]

        # Si la nouvelle direction et égale a la direction précédente tourner à gauche
        if nouvelle_direction == tourner(direction, droite=False):
            list_direction = list_direction + "G"
        # Pareil mais à droite
        elif nouvelle_direction == tourner(direction, droite=True):
            list_direction = list_direction + "D"
        # Demi tour si cul de sac
        elif nouvelle_direction == demitour(direction):
            list_direction = list_direction + "DD"

        # Dans tout les cas on avance
        list_direction = list_direction + "T"

        # On met a jour les infos
        direction = nouvelle_direction
        position = case

    return list_direction