import pygame

#configurer le nom de la fenetre
pygame.display.set_caption('test')

#Initialisation de la bibliothèque Pygame
pygame.init()


#pygame.mixer.init() # permet de lancer le son lors du lancement du programme
#son = pygame.mixer.Sound('testpygame/son/app.ogg')
#Création de la fenêtre
fenetre = pygame.display.set_mode((1920, 1080))


#Chargement et collage du fond
fond = pygame.image.load("testpygame/image/fond.jpg").convert()
fenetre.blit(fond, (0,0))


#chargement du perso
minotaure = pygame.image.load("testpygame/image/mino.jpg").convert_alpha()
f#position perso
position_mino = minotaure.get_rect()
fenetre.blit(minotaure,position_mino)
#deplacement du perso
nom_du_rect.move(déplacement_x,deplacement_y)
#taille du mino
#minotaurem=pygame.transform.scale(minotaure,(30,30))

#Rafraîchissement de l'écran
pygame.display.flip()



#Variable qui continue la boucle si = true , stoppe si = false
continuer = True

#Boucle 
while continuer:
    for event in pygame.event.get(): 
        if event.type == pygame.KEYDOWN:
            continuer = False
		if event.key == K_DOWN:	#Si "flèche bas"
				#On descend le mino
				position_mino = position_mino.move(0,3)
			

#partie permettent de quitter le programe lorsqu'on appuie sur la croix
pygame.quit()

