#!/usr/bin/env python

import csv1
import solution

def cli(grille):
    start = [1, 1]
    end = [len(grille)-2, len(grille[0])-2]

    csv1.printcsv(grille, start)
    print()

    ordres = ""
    while True:
        # On demande à l'utilisateur de rentrer les ordres.
        try:
            ordres = input(
            f"Entrer les directions pour finir le labyrinthe: ")
        # CTRL-D on quitte le programme.
        except EOFError:
            break

        # Si on a pas gagner on affiche l'erreur retourner.
        gagner, err = solution.verifie(grille, start, end, ordres)
        if not gagner:
            print(f"Erreur: {err} (ctrl-D pour quitter)")

        else:
            print("Vous avez gagné, félicitations.")
            break

cli(csv1.readcsv("./exemple/exemple1.csv"))