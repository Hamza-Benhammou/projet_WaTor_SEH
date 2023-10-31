import random
import os
import time

class Planet:
    def __init__(self, largeur_de_la_grille, hauteur_de_la_grille):
        self.largeur_de_la_grille = largeur_de_la_grille
        self.hauteur_de_la_grille = hauteur_de_la_grille
        self.grille = [[0 for _ in range(self.largeur_de_la_grille)] for _ in range(self.hauteur_de_la_grille)]
        self.poissons = []
        self.requins = []

    def peupler_le_monde(self, nombre_poissons, nombre_requins):        
        self.poissons = [Poisson(self,) for _ in range(nombre_poissons)]
        self.requins = [Requin(self) for _ in range(nombre_requins)]

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
        self.valeur_poisson = '\U0001f41f'
        self.age = 0    
        self.temps_reproduction = 8
       

    def deplacement(self):
        
        deplacement_possible = [[self.x + 1, self.y],[self.x - 1, self.y],[self.x, self.y + 1],[self.x, self.y - 1]]
        nouveau_x, nouveau_y = self.choisir_deplacement(deplacement_possible)
        self.deplacer_sur_case_vide(nouveau_x, nouveau_y)




    def choisir_deplacement(self, deplacement_possible):
        deplacement_choisi = random.choice(deplacement_possible)
        nouveau_x = deplacement_choisi[0]
        nouveau_y = deplacement_choisi[1]
        return nouveau_x, nouveau_y

    def deplacer_sur_case_vide(self, nouveau_x, nouveau_y):        
        if self.planet.verifer_case_vide(nouveau_x, nouveau_y):
            self.planet.mettre_a_jour_case(self.x, self.y, nouveau_x, nouveau_y, self.valeur_poisson)
            self.x = nouveau_x
            self.y = nouveau_y
            self.age += 1
            if self.age == self.temps_reproduction:
                self.reproduction()
                self.age = 0
        #     return True
        # return False

    def reproduction(self):
        deplacement_possible = [[self.x + 1, self.y],[self.x - 1, self.y],[self.x, self.y + 1],[self.x, self.y - 1]]
        
        nouveau_x, nouveau_y = self.choisir_deplacement(deplacement_possible)
        if self.planet.verifer_case_vide(nouveau_x, nouveau_y):
            new_poisson = Poisson(self.planet)
            new_poisson.x = nouveau_x
            new_poisson.y = nouveau_y
            self.planet.poissons.append(new_poisson)
            
class Requin(Poisson):
    def __init__(self, planet):
        super().__init__(planet)
        self.valeur_poisson = '🦈'
        self.starvation = 20
        self.age = 0 
        self.temps_reproduction = 12
                
    def deplacement(self):
        deplacement_possible = [[self.x + 1, self.y],[self.x - 1, self.y],[self.x, self.y + 1],[self.x, self.y - 1]]
        nouveau_x, nouveau_y = self.choisir_deplacement(deplacement_possible)
        self.deplacer_sur_case_vide(nouveau_x, nouveau_y)
        self.starvation -= 1
        if self.starvation == 0:
            self.mourir() 

    # def deplacer_sur_case_poisson(self, nouveau_x, nouveau_y):        
    #     if self.planet.verifer_case_poisson(nouveau_x, nouveau_y):
    #         self.planet.mettre_a_jour_case(self.x, self.y, nouveau_x, nouveau_y, self.valeur_poisson)
    #         self.x = nouveau_x
    #         self.y = nouveau_y
    #         self.age += 1
    #         if self.age == self.temps_reproduction:
    #             self.reproduction()
    #             self.age = 0
    #     #     return True
    #     # return False
        
    def mourir(self):
        self.planet.mettre_a_jour_case(self.x, self.y, self.x, self.y, 0)
        self.planet.requins.remove(self)

    def reproduction(self):
        deplacement_possible = [[self.x + 1, self.y],[self.x - 1, self.y],[self.x, self.y + 1],[self.x, self.y - 1]]        
        nouveau_x, nouveau_y = self.choisir_deplacement(deplacement_possible)
        if self.planet.verifer_case_vide(nouveau_x, nouveau_y):
            new_requin = Requin(self.planet)
            new_requin.x = nouveau_x
            new_requin.y = nouveau_y
            self.planet.requins.append(new_requin)
            

        
planete_1 = Planet(50, 50)
planete_1.peupler_le_monde(1,1)
planete_1.simuler(50)