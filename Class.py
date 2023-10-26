import random


class Planet:
    def __init__(self,largeur_de_la_grille, hauteur_de_la_grille):
        self.largeur_de_la_grille = largeur_de_la_grille
        self.hauteur_de_la_grille = hauteur_de_la_grille

    def display_planet(self): 
      self.display_planet = [[ 0 for hauteur in range(self.largeur_de_la_grille)] for largeur in range(self.hauteur_de_la_grille)]  
      for ligne in self.display_planet:
        print(*ligne)

planete_1 = Planet(10, 10)
planete_1.display_planet()




# class Fish(self, age, move, breeding):
#     self.age = age
#     self.move = move
#     self.breeding = breeding

#     def population(self):
#         population_shark = 7
#         population_fish = 18
#         population_totale = population_shark + population_fish
#         return population_totale
    
#     def reproduction(self):

# class Shark(Fish):
#     def __init__(self, age, move, breeding, power, eat):
#         super().__init__(self, age, move, breeding)
#         self.power = power
#         self.eat = eat

