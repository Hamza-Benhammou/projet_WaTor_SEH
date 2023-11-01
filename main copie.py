#code aujourdhui
#initialise classes et méthodes
import pygame
import random
import os
import time

"""class Planet:
    def __init__(self, largeur_de_la_grille, hauteur_de_la_grille):
        self.largeur_de_la_grille = largeur_de_la_grille
        self.hauteur_de_la_grille = hauteur_de_la_grille
        self.grille = [[0 for _ in range(self.largeur_de_la_grille)] for _ in range(self.hauteur_de_la_grille)]
        self.poissons = []
        self.requins = []

    def peupler_le_monde(self, nombre_poissons, nombre_requins):        
        self.poissons = [Poisson(self) for _ in range(nombre_poissons)]
        self.requins = [Requin(self) for _ in range(nombre_requins)]

    def afficher_le_monde(self):
        for ligne in self.grille:
            print(*ligne)        

    def verifer_case_vide(self, x, y):
        return self.grille[y % self.hauteur_de_la_grille][x % self.largeur_de_la_grille] == 0

    def mettre_a_jour_case(self, x_initial, y_initial, x_nouveau, y_nouveau, valeur_poisson):
        self.grille[y_initial % self.hauteur_de_la_grille][x_initial % self.largeur_de_la_grille] = 0
        self.grille[y_nouveau % self.hauteur_de_la_grille][x_nouveau % self.largeur_de_la_grille] = valeur_poisson

    def simuler(self, duree):
        for chronon in range(duree):
            os.system('clear')
            self.afficher_le_monde()
            for poisson in self.poissons:
                poisson.deplacement()
            for requin in self.requins:
                requin.deplacement()
            time.sleep(0.5)

class Poisson:
    def __init__(self, planet):
        self.x = random.choice(range(planet.largeur_de_la_grille))
        self.y = random.choice(range(planet.hauteur_de_la_grille))
        self.planet = planet
        self.age = 0

    def deplacement(self):
        deplacement_possible = [
            [self.x + 1, self.y],
            [self.x - 1, self.y],
            [self.x, self.y + 1],
            [self.x, self.y - 1]
        ]
        nouveau_x, nouveau_y = self.choisir_deplacement(deplacement_possible)
        if self.deplacer_sur_planete(nouveau_x, nouveau_y):
            self.age += 1
            if self.age == 8:
                self.reproduction()
                self.age = 0

    def choisir_deplacement(self, deplacement_possible):
        deplacement_choisi = random.choice(deplacement_possible)
        nouveau_x = deplacement_choisi[0]
        nouveau_y = deplacement_choisi[1]
        return nouveau_x, nouveau_y

    def deplacer_sur_planete(self, nouveau_x, nouveau_y):
        valeur_poisson = '\U0001f41f'
        if self.planet.verifer_case_vide(nouveau_x, nouveau_y):
            self.planet.mettre_a_jour_case(self.x, self.y, nouveau_x, nouveau_y, valeur_poisson)
            self.x = nouveau_x
            self.y = nouveau_y
            return True
        return False

    def reproduction(self):
        deplacement_possible = [
            [self.x + 1, self.y],
            [self.x - 1, self.y],
            [self.x, self.y + 1],
            [self.x, self.y - 1]
        ]
        
        nouveau_x, nouveau_y = self.choisir_deplacement(deplacement_possible)
        if self.planet.verifer_case_vide(nouveau_x, nouveau_y):
            new_poisson = Poisson(self.planet)
            new_poisson.x = nouveau_x
            new_poisson.y = nouveau_y
            self.planet.poissons.append(new_poisson)


class Requin(Poisson):    
    

    def deplacer_sur_planete(self, nouveau_x, nouveau_y):
        valeur_requin = '🦈'
        if self.planet.verifer_case_vide(nouveau_x, nouveau_y):
            self.planet.mettre_a_jour_case(self.x, self.y, nouveau_x, nouveau_y, valeur_requin)
            self.x = nouveau_x
            self.y = nouveau_y
            return True
        return False

    def reproduction(self):
        deplacement_possible = [
            [self.x + 1, self.y],
            [self.x - 1, self.y],
            [self.x, self.y + 1],
            [self.x, self.y - 1]
        ]
        
        nouveau_x, nouveau_y = self.choisir_deplacement(deplacement_possible)
        if self.planet.verifer_case_vide(nouveau_x, nouveau_y):
            new_requin = Requin(self.planet)
            new_requin.x = nouveau_x
            new_requin.y = nouveau_y
            self.planet.requins.append(new_requin)"""



#teste version pygame

pygame.init()

#crée la fenetre qu'on appelle surface
surface = pygame.display.set_mode((400,400))

#titre et icône
pygame.display.set_caption("Wator World")

#icone mer/poisson/requin

sea_image = pygame.image.load("vagues-deau.png")
fish = pygame.image.load("fish.png")
shark = pygame.image.load("shark.png")

surface.fill((250, 250, 250))

#crée une planete avec 1 poisson, 1 requin
#planete_1 = Planet(30, 30)
#planete_1.peupler_le_monde(1,1)




#boucle de jeu
running = True  #boucle pour terminer jeu au moment de cliquer sur croix (fermer)
clock = pygame.time.Clock()


while running:
    for event in pygame.even.get():
        if event.type == pygame.QUIT:
            running = False
#     #remplit grille couleur RGB
#     #grille.fill((250, 250, 250))
#     fish_coordinates = []

# # Générez d'abord une liste de toutes les coordonnées possibles
#     all_coordinates = [(x, y) for x in range(0, 400, 30) for y in range(0, 400, 30)]

# # Mélangez la liste des coordonnées pour les ordonner aléatoirement
#     random.shuffle(all_coordinates)

# # Sélectionnez les 10 premières coordonnées mélangées
#     for _ in range(1):
#         x, y = all_coordinates.pop()
#         fish_coordinates.append((x, y))
#     for x, y in fish_coordinates:
#         surface.blit(fish, (x, y))
#     for event in pygame.event.get():
#         if event.type == pygame.QUIT:
#             running = False
#      #placer poissons au hasard dans wator
#     #nb_poissons_depart = 15
#     # x = random.randrange(20,370,35)
#     # y = random.randrange(20,370,35)
#     #surface.blit(fish,(200,200))
    
   
    #test pour remplir la grille de poissons
    for i in range (20,370,35):
       for j in range (20,370,35):
            surface.blit(fish,(i,j))
    



    pygame.display.update()


pygame.quit()

