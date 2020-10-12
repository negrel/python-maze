from deplacement import *

OrdreInvalideErreur = "ordre invalide"

# Parse l'ordre donnée et retourne la position et la direction après avoir
# executé l'ordre
def ordre(position, direction, ordre):
    # On avance
    if ordre == "T":
        position = avancer(position, direction)
    # On tourne à gauche
    elif ordre == "G":
        direction = tourner(direction, droite=False)
    # On tourne a droite
    elif ordre == "D":
        direction = tourner(direction, droite=True)
    # Entrer non valide, on retourne une erreur
    else:
        return (None, None, OrdreInvalideErreur)

    return (position, direction, None)
