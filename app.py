#!/usr/bin/env python

from load import *

def cli(grille, start, end):
    print_grille(grille)
    print()

    ordres = ""
    while True:
        # On demande à l'utilisateur de rentrer les ordres.
        ordres = input(
        f"Entrer les directions pour finir le labyrinthe: ")

        gagner, err = verifie_solution(grille, start, end, ordres)
        if not gagner:
            print(err)

        else:
            print("Vous avez gagné, félicitations.")
            break
