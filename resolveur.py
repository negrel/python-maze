from deplacement import *

def mur_gauche(grille):
  start = [1, 1]
  end = [len(grille)-2, len(grille[0])-2]

  chemin = [start]

  position = start
  direction = directions["DROITE"]

  while not position == end:
    nouvelle_direction = tourner(direction, droite=False)
    y, x = avancer(position, nouvelle_direction)

    if grille[y][x] == 99:
      direction = nouvelle_direction
      position = [y, x]
      chemin.append(position)
    else:
      direction = tourner(direction, droite=True)
      
  return chemin


def mur_gauche_essai(matrix):
    # position_defini
    w = len(matrix[0])
    v = len(matrix)

    # position_initial
    x = 1
    y = 1

    direction = 0

    while not (x == w and y == v):
        if direction == 0:
            if matrix[y][x - 1] == 99:
                x = x - 1
                direction = 1

            elif matrix[y - 1][x] == 99:
                y = y - 1

            elif matrix[y][x + 1] == 99:
                x = x + 1
                direction = 3

            else:
                direction = 1

        elif direction == 1:

            if matrix[y + 1][x] == 99:
                y = y + 1
                direction = 2

            elif matrix[y][x - 1] == 99:
                x = x - 1

            elif matrix[y - 1][x] == 99:
                y = y - 1
                direction = 0

            else:
                direction = 2

        elif direction == 2:

            if matrix[y][x + 1] == 99:
                x = x + 1
                direction = 3

            elif matrix[y + 1][x] == 99:
                y = y + 1

            elif matrix[y][x - 1] == 99:
                x = x - 1
                direction = 1

            else:
                direction = 3

        elif direction == 3:

            if matrix[y - 1][x] == 99:
                y = y - 1
                direction = 0

            elif matrix[y][x + 1] == 99:
                x = x + 1

            elif matrix[y + 1][x] == 99:
                y = y + 1
                direction = 2

            else:
                direction = 0

        print(y, x, direction)
