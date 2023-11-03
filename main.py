import random
import os
import time
import pygame
import sys

class Planet:
    def __init__(self, largeur_de_la_grille, hauteur_de_la_grille):
        self.largeur_de_la_grille = largeur_de_la_grille
        self.hauteur_de_la_grille = hauteur_de_la_grille
        self.grille = [[0 for case in range(self.largeur_de_la_grille)] for _ in range(self.hauteur_de_la_grille)]
        self.poissons = []
        self.requins = []

    def peupler_le_monde(self, nombre_poissons, nombre_requins):        
        self.poissons = [Poisson(self) for poisson in range(nombre_poissons)]
        self.requins = [Requin(self) for requin in range(nombre_requins)]

    def afficher_le_monde(self):
        for ligne in self.grille:
            print(*ligne)        

    def verifer_case_vide(self, x, y):
        return self.grille[y % self.hauteur_de_la_grille][x % self.largeur_de_la_grille] == 0
    
    def verifer_case_poisson(self, x, y):
        return self.grille[y % self.hauteur_de_la_grille][x % self.largeur_de_la_grille] == '\U0001f41f'

    def mettre_a_jour_case(self, x_initial, y_initial, x_nouveau, y_nouveau, valeur_poisson):
        self.grille[y_initial % self.hauteur_de_la_grille][x_initial % self.largeur_de_la_grille] = 0
        self.grille[y_nouveau % self.hauteur_de_la_grille][x_nouveau % self.largeur_de_la_grille] = valeur_poisson

    def simuler(self, duree):
        for chronon in range(duree):
            os.system('clear') #('cls' sur windows)
            self.afficher_le_monde()
            for poisson in self.poissons:
                poisson.deplacement()    
            for requin in self.requins:
                requin.deplacement()        
            time.sleep(0.2)

class Poisson:
    def __init__(self, planet):
        self.x = random.choice(range(planet.largeur_de_la_grille))
        self.y = random.choice(range(planet.hauteur_de_la_grille))
        self.planet = planet
        self.valeur_poisson = '\U0001f41f'
        self.age = 0    
        self.temps_reproduction = 8
       

    def choisir_deplacement_case_vide(self):
        case_vide = []

        if self.planet.verifer_case_vide(self.x + 1, self.y):
            case_vide.append([self.x + 1, self.y])
        if self.planet.verifer_case_vide(self.x - 1, self.y):
            case_vide.append([self.x - 1, self.y])
        if self.planet.verifer_case_vide(self.x, self.y + 1):
            case_vide.append([self.x, self.y + 1])
        if self.planet.verifer_case_vide(self.x, self.y - 1):
            case_vide.append([self.x, self.y - 1])
        return case_vide

    def deplacement(self):
        choix = self.choisir_deplacement_case_vide()
        if choix:
            nouveau_x, nouveau_y = random.choice(choix)
            self.planet.mettre_a_jour_case(self.x, self.y, nouveau_x, nouveau_y, self.valeur_poisson)
            self.x = nouveau_x
            self.y = nouveau_y
            self.age += 1
            if self.age == self.temps_reproduction:
                self.reproduction()
                self.age = 0
    
    def reproduction(self):

        new_poisson = Poisson(self.planet)
        new_poisson.x = self.x
        new_poisson.y = self.y
        self.planet.poissons.append(new_poisson)

        # choix_reproduction = self.choisir_deplacement_case_vide()
        # if choix_reproduction:
        #     nouveau_x, nouveau_y = random.choice(choix_reproduction)
        #     if self.planet.verifer_case_vide(nouveau_x, nouveau_y):
        #         new_poisson = Poisson(self.planet)
        #         new_poisson.x = nouveau_x
        #         new_poisson.y = nouveau_y
        #         self.planet.poissons.append(new_poisson)
           
class Requin(Poisson):
    def __init__(self, planet):
        super().__init__(planet)
        self.valeur_poisson = '🦀'
        self.starvation = 8
        self.temps_reproduction = 60
    
    def choisir_deplacement_case_poisson(self):
        case_poisson = []

        if self.planet.verifer_case_poisson(self.x + 1, self.y):
            case_poisson.append([self.x + 1, self.y])
        if self.planet.verifer_case_poisson(self.x - 1, self.y):
            case_poisson.append([self.x - 1, self.y])
        if self.planet.verifer_case_poisson(self.x, self.y + 1):
            case_poisson.append([self.x, self.y + 1])
        if self.planet.verifer_case_poisson(self.x, self.y - 1):
            case_poisson.append([self.x, self.y - 1])
        return case_poisson
    
    def choix_de_la_case(self):
        casepoisson = self.choisir_deplacement_case_poisson()
        casevide = self.choisir_deplacement_case_vide()
        if casepoisson:
            return casepoisson
        elif casevide:
            return casevide
        else:
            return

    def deplacement(self):
        choix = self.choix_de_la_case()
        if choix:
            nouveau_x, nouveau_y = random.choice(choix)
            self.planet.mettre_a_jour_case(self.x, self.y, nouveau_x, nouveau_y, self.valeur_poisson)
            self.x = nouveau_x
            self.y = nouveau_y
            self.age += 1
        

            poissons_sur_case = [poisson for poisson in self.planet.poissons if poisson.x == self.x and poisson.y == self.y]
    
            if poissons_sur_case:
                poisson = poissons_sur_case[0]  
                self.manger(poisson)

            
            if self.age == self.temps_reproduction:
                    self.reproduction()
                    self.age = 0

            self.starvation -= 1
            if self.starvation == 0:
                self.mourir()

    def manger(self, poisson):
        self.planet.poissons.remove(poisson)
        self.starvation += 4

    def mourir(self):
        self.planet.mettre_a_jour_case(self.x, self.y, self.x, self.y, 0)
        self.planet.requins.remove(self)    

    def reproduction(self):             
        new_requin = Requin(self.planet)
        new_requin.x = self.x
        new_requin.y = self.y
        self.planet.requins.append(new_requin)

planete_1 = Planet(50, 50)
planete_1.peupler_le_monde(150,30)
planete_1.simuler(20)


"""class PygameDisplay:
    def __init__(self, planet):
        self.planet = planet
        self.taille_case = 20
        self.largeur_de_la_grille = planet.largeur_de_la_grille
        self.hauteur_de_la_grille = planet.hauteur_de_la_grille
        self.fenetre = pygame.display.set_mode((self.largeur_de_la_grille * self.taille_case, self.hauteur_de_la_grille * self.taille_case))
        self.clock = pygame.time.Clock()

    def afficher_le_monde(self):
        for y, ligne in enumerate(self.planet.grille):
            for x, case in enumerate(ligne):
                pygame.draw.rect(self.fenetre, (255, 255, 255) if case == 0 else (0, 0, 255), (x * self.taille_case, y * self.taille_case, self.taille_case, self.taille_case))
        pygame.display.flip()

    def boucle_principale(self):
        running = True
        while running:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    running = False

            self.planet.simuler(4)
            self.afficher_le_monde()
            self.clock.tick(10)  # Limite la vitesse d'affichage à 10 images par seconde

        pygame.quit()
        sys.exit()"""


class PygameDisplay:

    def __init__(self, planet):
        self.planet = planet
        self.taille_case = 60
        self.largeur_de_la_grille = planet.largeur_de_la_grille
        self.hauteur_de_la_grille = planet.hauteur_de_la_grille
        self.fenetre = pygame.display.set_mode((self.largeur_de_la_grille * self.taille_case, self.hauteur_de_la_grille * self.taille_case))
       # self.clock = pygame.time.Clock()

        # Chargez les images pour les poissons, les requins et la mer
        self.image_poisson = pygame.image.load('poisson-clown.png')
        self.image_requin = pygame.image.load('requin.png')
        self.image_mer = pygame.image.load('sea.png')        

    def afficher_le_monde(self):
        self.fenetre.fill((255, 255, 255))
#         #for y, ligne in enumerate(self.planet.grille):
#         #    for x, case in enumerate(ligne):
#         #        if case == '\U0001f41f':
#         #            self.fenetre.blit(self.image_poisson, (x * self.taille_case, y * self.taille_case))              
#         #        elif case == '🦀':
#         #            self.fenetre.blit(self.image_requin, (x * self.taille_case, y * self.taille_case))
#         #        else:
#         #           self.fenetre.blit(self.image_mer, (x * self.taille_case, y * self.taille_case))
        for y in range(self.planet.hauteur_de_la_grille):
            for x in range(self.planet.largeur_de_la_grille):
                # Affiche la mer sur toute la grille
                if self.planet.grille[y][x] == 0:
                    self.fenetre.blit(self.image_mer, (x * self.taille_case, y * self.taille_case))
                # Si la case contient un poisson, affiche l'image du poisson
                elif self.planet.grille[y][x] == '\U0001f41f':
                    self.fenetre.blit(self.image_poisson, (x * self.taille_case, y * self.taille_case))
                # Si la case contient un requin, affiche l'image du requin
                elif self.planet.grille[y][x] == '🦀':
                    self.fenetre.blit(self.image_requin, (x * self.taille_case, y * self.taille_case))
        pygame.display.flip()


    def boucle_principale(self):
        running = True
        while running:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    running = False

            self.planet.simuler(1)
            self.afficher_le_monde()
            #self.clock.tick(20)
            pygame.time.delay(200)

    


        pygame.quit()
        sys.exit()

        

# Code pour initialiser la planète, les poissons et les requins
planete_1 = Planet(15, 15)
planete_1.peupler_le_monde(15, 2)

# Code pour lancer la simulation avec Pygame
pygame.init()
pygame.display.set_caption("WATOR")
pygame_display = PygameDisplay(planete_1)
pygame_display.boucle_principale()
