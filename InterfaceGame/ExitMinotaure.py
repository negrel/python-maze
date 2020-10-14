import math
import turtle
import pygame


# Ouverture de la page d'accueil
pygame.init()

ecran = pygame.display.set_mode((700, 700))
continuer = True
pygame.display.set_caption("Aide le gentil minotaure a sortir du labyrinthe")
image = pygame.image.load("InterfaceGame/Assets/Image/minotaure.png")
while continuer:
    for event in pygame.event.get():
        if event.type == pygame.KEYDOWN:
        if event.type == pygame.KEYDOWN:
            continuer = False

pygame.quit()

#Ouverture de la page de jeu
 
Windows =  turtle.Screen()
Windows.bgcolor("black")
Windows.title("Aide le gentil minotaure a sortir du labyrinthe")
Windows.setup(700,700)

#Register shape
#turtle.Register_shape("/home/vivien/Documents/prj1annee/maze/InterfaceGame/Assets/Image/wall-1.gif")

#Creation des carrés du Labyrinthe
class Labyrinthe(turtle.Turtle):
    def __init__(self):
        turtle.Turtle.__init__(self)
        self.shape("square")
        self.color("white")
        self.penup()
        self.speed(0)
    
class Minotaure(turtle.Turtle):
    def __init__(self):
        turtle.Turtle.__init__(self)
        self.shape("square")
        self.color("green")
        self.penup()
        self.speed(0)

#Initialisation du tableau
Tableaus = [""]
 
#Tableau numero 1
Tableau1 = [
"XXXXXXXXX",
"XP    X X",
"X XXX X X",
"X X   X X",
"X    XX X",
"XXXX  X X",
"X  X XX X",
"X       X",
"XXXXXXXXX",

]
 
 
Tableaus.append(Tableau1)
 
def setup_maze(Tab):
    for y in range(len(Tab)):
        for x in range(len(Tab[y])):
            character = Tab [y] [x]

            #Calcule les coord x, y
            screen_x = -200 + (x * 24)
            screen_y = 200 - (y * 24)

            # Vérifie si X représente un Mur
            if character == "X":
                labyrinthe.goto(screen_x, screen_y)
                #labyrinthe.shape("/home/vivien/Documents/prj1annee/maze/InterfaceGame/Assets/Image/wall-1.gif")
                labyrinthe.stamp()

            # Vérifie si M représente le Minotaure
            if character == "P":
                minotaure.goto(screen_x, screen_y)
  
labyrinthe = Labyrinthe()
minotaure = Minotaure()

setup_maze(Tableaus[1])

#Main Game Loop
while True:
    pass