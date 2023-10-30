import random
import os
import time

class Planet:
    def __init__(self, largeur_de_la_grille, hauteur_de_la_grille):
        self.largeur_de_la_grille = largeur_de_la_grille
        self.hauteur_de_la_grille = hauteur_de_la_grille
        self.grille = [[0 for _ in range(self.largeur_de_la_grille)] for _ in range(self.hauteur_de_la_grille)]
        self.poissons = []

    def peupler_le_monde(self, nombre_poissons):        
        self.poissons = [Poisson(self) for _ in range(nombre_poissons)]

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

def monde_1():
    planete_1 = Planet(10, 10)
    poissons = [Poisson(planete_1) for _ in range(1)]

    chronon = 0

    while chronon < 50:
        os.system('clear')
        planete_1.display()
        for poisson in poissons:
            poisson.deplacement()

        chronon += 1
        time.sleep(.5)

# Appel du monde 1
# monde_1()

def monde_2():
    planete_1 = Planet(30, 30)
    for _ in range(50):
        poisson = Poisson(planete_1)
        planete_1.poissons.append(poisson)

    chronon = 0

    while chronon < 100:
        os.system('clear')
        planete_1.display()
        for poisson in planete_1.poissons:
            poisson.deplacement()

        chronon += 1
        time.sleep(.5)

# Appel du monde 2
monde_2()
planete_1 = Planet(30, 30)
planete_1.peupler_le_monde(10)
planete_1.simuler(500)
