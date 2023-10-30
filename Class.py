import random


class Planet:
    def __init__(self,largeur_de_la_grille, hauteur_de_la_grille):
        self.largeur_de_la_grille = largeur_de_la_grille
        self.hauteur_de_la_grille = hauteur_de_la_grille
    

    def display(self): 
      self.display = [[ 0 for hauteur in range(self.largeur_de_la_grille)] for largeur in range(self.hauteur_de_la_grille)]  
      for ligne in self.display:
        print(*ligne)

planete_1 = Planet(10, 10)
planete_1.display


class Fish:
    def __init__(self, planet, x, y):
      self.planet = planet
      self.x = x
      self.y = y
    

    # Je crée une méthode move pour le déplacement des poissons
    def move(self, new_x, new_y):      
        # J'utilise random pour générer un déplacement aléatoire
      directions = [(0, 1), (0, -1), (1, 0), (-1, 0)]
      dx, dy = random.choice(directions)
      new_x = self.x + dx
      new_y = self.y + dy 
        # Je met à jour les nouvelles positions des poissons
      self.x = new_x
      self.y = new_y


       


