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
        deplacement_possible = [[self.x + 1,self.y],[self.x - 1, self.y],[self.x, self.y + 1],[self.x, self.y -1]]

        while True:
            deplacement_choisi = random.choice(deplacement_possible)
            nouveau_x = deplacement_choisi[0]
            nouveau_y = deplacement_choisi[1]

            if self.planet.display_planet[nouveau_y % self.planet.hauteur_de_la_grille][nouveau_x % self.planet.largeur_de_la_grille] == 0:
                # Je change la case initiale par 0
                self.planet.display_planet[self.y][self.x] = 0
                # Je déplace le poisson
                self.x = nouveau_x % self.planet.largeur_de_la_grille
                self.y = nouveau_y % self.planet.hauteur_de_la_grille
                # Je change la nouvelle par "🐟"
                self.planet.display_planet[self.y][self.x] = valeur_poisson
                break

        
        # deplacement_choisi = random.choice(deplacement_possible)
        # self.x = deplacement_choisi[0]
        # self.y = deplacement_choisi[1]

        # if deplacement_choisi == deplacement_possible[0]:
        #     self.planet.display_planet[self.y % self.planet.hauteur_de_la_grille][self.x % self.planet.largeur_de_la_grille] = valeur_poisson
        #     self.planet.display_planet[self.y % self.planet.hauteur_de_la_grille][(self.x - 1) % self.planet.largeur_de_la_grille] = 0
        
            
        # elif deplacement_choisi == deplacement_possible[1]:
        #     self.planet.display_planet[self.y % self.planet.hauteur_de_la_grille][self.x % self.planet.largeur_de_la_grille] = valeur_poisson
        #     self.planet.display_planet[self.y % self.planet.hauteur_de_la_grille][(self.x + 1) % self.planet.largeur_de_la_grille] = 0            

        # elif deplacement_choisi == deplacement_possible[2]:
        #     self.planet.display_planet[self.y % self.planet.hauteur_de_la_grille][self.x % self.planet.largeur_de_la_grille] = valeur_poisson
        #     self.planet.display_planet[(self.y - 1) % self.planet.hauteur_de_la_grille][self.x % self.planet.largeur_de_la_grille] = 0            

        # elif deplacement_choisi == deplacement_possible[3]:
        #     self.planet.display_planet[self.y % self.planet.hauteur_de_la_grille][self.x % self.planet.largeur_de_la_grille] = valeur_poisson
        #     self.planet.display_planet[(self.y + 1) % self.planet.hauteur_de_la_grille][self.x % self.planet.largeur_de_la_grille] = 0

        # for ligne in self.planet.display_planet:
        #     print(*ligne)
        # print("-------------------------------")


# charge de reproduction
        # charge +=1

        # for ligne in grille:
        #     print(*ligne)
        # print("-------------------------------")
            

# Paramétrages du monde 1
def monde_1():
    planete_1 = Planet(50, 50)
    poissons = [Poisson(planete_1) for _ in range(100)]

    chronon = 0

    while chronon < 50:
        planete_1.display()
        for poisson in poissons:
            poisson.deplacement()
        
        chronon += 1

# Appel du monde 1
monde_1()