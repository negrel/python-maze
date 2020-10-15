import time
import pygame
import turtle

#Initialisation de la bibliothèque Pygame

#configurer le nom de la fenetre
pygame.display.set_caption('test')
pygame.init()


#chargement du perso
#minotaure = pygame.image.load("testpygame/image/mino.jpg").convert_alpha()

#Ouverture de la page de jeu
 
Windows =  turtle.Screen()
Windows.bgcolor("black")
Windows.title("Aide le gentil minotaure a sortir du labyrinthe")
Windows.setup(1920,1020)

#Chargement et collage du fond
#fond = pygame.image.load("testpygame/image/fond.jpg").convert()
Windows.blit(fond, (0,0))

game_running = True
#def f(game_running):
    while game_running:
        # On boucle à travers tout les évenements
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                game_running = False
            if event.type == pygame.VIDEORESIZE:
                WINDOW_WIDTH, WINDOW_HEIGHT = event.size

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
"X       X",
"X       X",
"X   M   X",
"X       X",
"X       X",
"X   C   X",
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
            if character == "M":
                minotaure.goto(screen_x, screen_y)
            # Vérifie si C représente la cible
            if character == "C":
                minotaure.goto(screen_x, screen_y)
  
  
labyrinthe = Labyrinthe()
minotaure = Minotaure()

setup_maze(Tableaus[1])