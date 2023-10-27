import random
import os
import time

class Planet:
    def __init__(self, largeur_de_la_grille, hauteur_de_la_grille):
        self.largeur_de_la_grille = largeur_de_la_grille
        self.hauteur_de_la_grille = hauteur_de_la_grille
        self.display_planet = [[0 for hauteur in range(self.largeur_de_la_grille)] for largeur in range(self.hauteur_de_la_grille)]

    def display(self):
        for ligne in self.display_planet:
            print(*ligne)
        

    def est_case_vide(self, x, y):
        return self.display_planet[y % self.hauteur_de_la_grille][x % self.largeur_de_la_grille] == 0

    def deplacer_poisson(self, x_initial, y_initial, x_nouveau, y_nouveau, valeur_poisson):
        self.display_planet[y_initial % self.hauteur_de_la_grille][x_initial % self.largeur_de_la_grille] = 0
        self.display_planet[y_nouveau % self.hauteur_de_la_grille][x_nouveau % self.largeur_de_la_grille] = valeur_poisson

class Poisson:
    def __init__(self, planet):
        self.x = random.choice(range(planet.largeur_de_la_grille))
        self.y = random.choice(range(planet.hauteur_de_la_grille))
        self.planet = planet
        self.age = 0

    def deplacement(self):
        deplacement_possible = [[self.x + 1, self.y], [self.x - 1, self.y], [self.x, self.y + 1], [self.x, self.y - 1]]
        nouveau_x, nouveau_y = self.choisir_deplacement(deplacement_possible)
        if self.deplacer_poisson(nouveau_x, nouveau_y):
            self.age += 1
        if self.age == 8:
            self.reproduction()
            self.age = 0

    def choisir_deplacement(self, deplacement_possible):
        deplacement_choisi = random.choice(deplacement_possible)
        nouveau_x = deplacement_choisi[0]
        nouveau_y = deplacement_choisi[1]
        return nouveau_x, nouveau_y

    def deplacer_poisson(self, nouveau_x, nouveau_y):
        valeur_poisson = "🐟"
        if self.planet.est_case_vide(nouveau_x, nouveau_y):
            self.planet.deplacer_poisson(self.x, self.y, nouveau_x, nouveau_y, valeur_poisson)
            self.x = nouveau_x
            self.y = nouveau_y
            return True
        return False

    def reproduction(self):
        deplacement_possible = [[self.x + 1, self.y], [self.x - 1, self.y], [self.x, self.y + 1], [self.x, self.y - 1]]
        for _ in range(1):
            nouveau_x, nouveau_y = self.choisir_deplacement(deplacement_possible)
            if self.planet.est_case_vide(nouveau_x, nouveau_y):
                new_poisson = Poisson(self.planet)
                new_poisson.x = nouveau_x
                new_poisson.y = nouveau_y
                new_poisson.deplacer_poisson(nouveau_x, nouveau_y)




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
monde_1()

def monde_2():
    planete_1 = Planet(30, 30)
    poissons = [Poisson(planete_1) for _ in range(10)]

    chronon = 0

    while chronon < 100:
        os.system('clear')
        planete_1.display()
        for poisson in poissons:
            poisson.deplacement()

        chronon += 1
        time.sleep(.5)

# Appel du monde 1
# monde_2()