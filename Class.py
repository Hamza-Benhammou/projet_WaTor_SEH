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


class Fish:
   def __init__(self, planet, x, y):
    self.planet = planet
    self.x = x
    self.y = y
    self.chronon = 0

    # Je crée une méthode move pour le déplacement des poissons
    def move(self):      
        # J'utilise random pour générer un déplacement aléatoire
       directions = (0, 1), (0, -1), (1, 0), (-1, 0)
       dx, dy = random.choice(directions)
       new_x = self.x + dx
       new_y = self.y + dy
    
        # Je met à jour les nouvelles positions des poissons
       self.x = new_x
       self.y = new_y

        # Je met à jour la planète avec les nouvelles positions des poissons dessus
       self.planet.display_planet[new_y][new_x] = 1
        # J'incrémente de 1 pour qu'un nouveau chronon s'écoule
       self.chronon += 1

    # # Je crée une méthode breeding pour la reproduction des poissons
    # def breeding(self):
    #      # Je crée une condition pour que mes poissons se reproduisent 
    #     # qu'après 8 chronons
    #     if self.chronon == 8:
    #     # Je déclare une nouvelle variable available_position pour afficher
    #     # les positions vides sur la planète
    #         available_position = 
       
       


