import random

class Planet:
    def __init__(self,largeur_de_la_grille, hauteur_de_la_grille):
        self.largeur_de_la_grille = largeur_de_la_grille
        self.hauteur_de_la_grille = hauteur_de_la_grille
        self.display_planet = [[ 0 for hauteur in range(self.largeur_de_la_grille)] for largeur in range(self.hauteur_de_la_grille)]         

    def display(self): 
        for ligne in self.display_planet:
            print(*ligne)
        print("\n-------------------\n")

class Poisson:
    def __init__(self, planet):
        self.x = random.choice(range(planet.largeur_de_la_grille))
        self.y = random.choice(range(planet.hauteur_de_la_grille))
        self.planet = planet

    def deplacement(self):
        valeur_poisson =  "🐟"
        # self.display_planet[self.y % self.hauteur_de_la_grille][self.x % Planet.largeur_de_la_grille] = valeur_poisson
        
        deplacement_possible = [[self.x + 1,self.y],[self.x - 1, self.y],[self.x, self.y + 1],[self.x, self.y -1]]

        deplacement_choisi = random.choice(deplacement_possible)
        self.x = deplacement_choisi[0]
        self.y = deplacement_choisi[1]

        if deplacement_choisi == deplacement_possible[0]:
            self.planet.display_planet[self.y % self.planet.hauteur_de_la_grille][self.x % self.planet.largeur_de_la_grille] = valeur_poisson
            self.planet.display_planet[self.y % self.planet.hauteur_de_la_grille][(self.x - 1) % self.planet.largeur_de_la_grille] = 0
        
            
        elif deplacement_choisi == deplacement_possible[1]:
            self.planet.display_planet[self.y % self.planet.hauteur_de_la_grille][self.x % self.planet.largeur_de_la_grille] = valeur_poisson
            self.planet.display_planet[self.y % self.planet.hauteur_de_la_grille][(self.x + 1) % self.planet.largeur_de_la_grille] = 0            

        elif deplacement_choisi == deplacement_possible[2]:
            self.planet.display_planet[self.y % self.planet.hauteur_de_la_grille][self.x % self.planet.largeur_de_la_grille] = valeur_poisson
            self.planet.display_planet[(self.y - 1) % self.planet.hauteur_de_la_grille][self.x % self.planet.largeur_de_la_grille] = 0            

        elif deplacement_choisi == deplacement_possible[3]:
            self.planet.display_planet[self.y % self.planet.hauteur_de_la_grille][self.x % self.planet.largeur_de_la_grille] = valeur_poisson
            self.planet.display_planet[(self.y + 1) % self.planet.hauteur_de_la_grille][self.x % self.planet.largeur_de_la_grille] = 0

        # for ligne in self.planet.display_planet:
        #     print(*ligne)
        # print("-------------------------------")


# charge de reproduction
        # charge +=1

        # for ligne in grille:
        #     print(*ligne)
        # print("-------------------------------")
            



planete_1 = Planet(10, 10)
poissons = [Poisson(planete_1) for _ in range(5)]

chronon = 0

while chronon < 50:
    for poisson in poissons:
        poisson.deplacement()
    planete_1.display()
    chronon += 1