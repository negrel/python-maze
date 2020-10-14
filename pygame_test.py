import pygame

#configurer le nom de la fenetre
pygame.display.set_caption('test')

#Initialisation de la bibliothèque Pygame
pygame.init()

pygame.mixer.init() # permet de lancer le son lors du lancement du programme
#son = pygame.mixer.Sound('file.ogg')
#Création de la fenêtre
fenetre = pygame.display.set_mode((640, 480))

#chargement 'du fond
#fenetre.blit(fond, (40,30))

#Rafraîchissement de l'écran
pygame.display.flip()

#On positionne l'image dans la fenetre
def fond_menu(x,y,image):
  surface.blit(image, (x,y))
x=0
y=0
v=0

#Variable qui continue la boucle si = 1, stoppe si = 0
continuer = 1

#Boucle infinie
while continuer:
	continuer = int(input())
    

#partie permettent de quitter le programe lorsqu'on appuie sur la croix
pygame.quit()