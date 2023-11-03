import random
import os
import time

class Planet:
    def __init__(self, largeur_de_la_grille, hauteur_de_la_grille):
        self.largeur_de_la_grille = largeur_de_la_grille
        self.hauteur_de_la_grille = hauteur_de_la_grille
        self.grille = [[0 for case in range(self.largeur_de_la_grille)] for _ in range(self.hauteur_de_la_grille)]
        self.poissons = []
        self.requins = []

    def peupler_le_monde(self, nombre_poissons, nombre_requins):        
        self.poissons = [Poisson(self,) for poisson in range(nombre_poissons)]
        self.requins = [Requin(self) for requin in range(nombre_requins)]
        # Cette méthode ajoute le nombre de poissons et de requins dans chaque liste vide.

    def afficher_le_monde(self):
        for ligne in self.grille:
            print(*ligne)
        print(f"\nPopulation de poissons: {len(self.poissons)}, \nPopulation de requins: {len(self.requins)}")
        # A chaque chronon, cette méthode affiche l'état actuel du monde et sa population.

    def verifer_case_vide(self, y, x):
        return self.grille[y % self.hauteur_de_la_grille][x % self.largeur_de_la_grille] == 0
    # Cette méthode vérifie si une case [y,x] est vide
    
    def verifer_case_poisson(self, y, x):
        return self.grille[y % self.hauteur_de_la_grille][x % self.largeur_de_la_grille] == '\U0001f41f'
    # Cette méthode vérifie si une case [y,x] contient un poisson

    def mettre_a_jour_case(self, y_initial, x_initial, y_nouveau, x_nouveau, valeur_poisson):
        self.grille[y_initial % self.hauteur_de_la_grille][x_initial % self.largeur_de_la_grille] = 0
        self.grille[y_nouveau % self.hauteur_de_la_grille][x_nouveau % self.largeur_de_la_grille] = valeur_poisson

    def simuler(self, duree):
        for chronon in range(duree):
            os.system('cls')   
            for requin in self.requins:
                requin.deplacement()         
            for poisson in self.poissons:
                poisson.deplacement()             
            self.afficher_le_monde()       
            time.sleep(.2)
    # Cette méthode lance la simulation. duree = nombre de chronons

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
        if self.planet.verifer_case_vide(self.y + 1, self.x):
            case_vide.append([(self.y + 1) % self.planet.hauteur_de_la_grille , self.x])

        if self.planet.verifer_case_vide(self.y - 1, self.x):
            case_vide.append([(self.y - 1) % self.planet.hauteur_de_la_grille, self.x])

        if self.planet.verifer_case_vide(self.y, self.x + 1):
            case_vide.append([self.y, (self.x + 1) % self.planet.largeur_de_la_grille])

        if self.planet.verifer_case_vide(self.y, self.x - 1):
            case_vide.append([self.y, (self.x - 1) % self.planet.largeur_de_la_grille])

        if case_vide:
            return case_vide
        else:
            return
        # Cette méthode permet de scanner les 4 cases autour du poisson et ajoute les cases vides dans une liste
        # return case_vide permet de récupérer la liste si elle contient des coordonnées quand on appelle la méthode
        

    def deplacement(self):
        if self.choisir_deplacement_case_vide():
            nouveau_y, nouveau_x = random.choice(self.choisir_deplacement_case_vide())
            self.planet.grille[self.y][self.x] = 0
            if self.age == self.temps_reproduction:
                self.reproduction()
                self.age = 0
            self.x = nouveau_x
            self.y = nouveau_y
            self.planet.grille[self.y][self.x] = self.valeur_poisson

        else:
            return
        self.age += 1  

        # Si la liste case_vide contient des coordonnées, le poisson se reproduit s'il a atteint l'age et se déplace 
    
    def reproduction(self):
        new_poisson = Poisson(self.planet)
        new_poisson.x = self.x
        new_poisson.y = self.y
        self.planet.poissons.append(new_poisson)
        self.planet.grille[self.y][self.x] = self.valeur_poisson
        # Quand un poisson se reproduit, le nouveau poisson récupère les coordoonées du parent et est ajouté à la liste Poisson

           
class Requin(Poisson):
    def __init__(self, planet):
        super().__init__(planet)
        self.valeur_poisson = '🦀'
        self.starvation = 10
        self.temps_reproduction = 40
    
    def choisir_deplacement_case_poisson(self):
        case_poisson = []
        if self.planet.verifer_case_poisson(self.y + 1, self.x):
            case_poisson.append([(self.y + 1) % self.planet.hauteur_de_la_grille, self.x])

        if self.planet.verifer_case_poisson(self.y - 1, self.x):
            case_poisson.append([(self.y - 1) % self.planet.hauteur_de_la_grille, self.x])

        if self.planet.verifer_case_poisson(self.y, self.x + 1):
            case_poisson.append([self.y, (self.x + 1) % self.planet.largeur_de_la_grille])

        if self.planet.verifer_case_poisson(self.y, self.x - 1):
            case_poisson.append([self.y, (self.x - 1) % self.planet.largeur_de_la_grille])
        return case_poisson
        # Cette méthode permet de scanner les 4 cases autour du requin et ajoute les cases occupées par un poisson dans une liste
        # return case_vide permet de récupérer la liste si elle contient des coordonnées quand on appelle la méthode
    
    def choix_de_la_case(self):
        casepoisson = self.choisir_deplacement_case_poisson()
        casevide = self.choisir_deplacement_case_vide()
        if casepoisson:
            return casepoisson
        elif casevide:
            return casevide
        # Le requin choisit en priorité une case occupée par un poisson, sinon il choisit les coordonnées d'une case vide
        # Mais il ne se déplace pas encore


    def deplacement(self):
        choix = self.choix_de_la_case()        
        if choix:
            nouveau_y, nouveau_x = random.choice(choix)
            self.planet.grille[self.y][self.x] = 0
            if self.age == self.temps_reproduction:
                self.reproduction()
                self.age = 0
            
            self.x = nouveau_x
            self.y = nouveau_y
            self.planet.grille[self.y][self.x] = self.valeur_poisson
            
        else:
            return
        self.age += 1

        
        poissons_sur_case = [poisson for poisson in self.planet.poissons if poisson.y == self.y and poisson.x == self.x]
    
        if poissons_sur_case:
            poisson = poissons_sur_case[0]
            self.manger(poisson)

        self.starvation -= 1
        if self.starvation == 0:
            self.mourir()

        # Si le requin peut se déplacer, il se reproduit s'il a atteint l'age et se déplace sur une case poisson ou une case vide
        # Si un requin se déplace sur un case poisson, ce poisson est ajouté à une liste et il est ensuite mangé.
        # Le requin perd un point d'énergie, s'il atteint 0, il meurt


    def manger(self, poisson):
        self.planet.poissons.remove(poisson)
        self.starvation += 3
    # Le poisson mangé est retiré de la liste Poisson
    # Le requin regagne 3 points d'énergie

    def reproduction(self):             
        new_requin = Requin(self.planet)
        new_requin.y = self.y
        new_requin.x = self.x
        self.planet.requins.append(new_requin)
        self.planet.grille[self.y][self.x] = self.valeur_poisson
        # Quand un poisson se reproduit, le nouveau poisson récupère les coordoonées du parent et est ajouté à la liste Poisson
        
    def mourir(self):
        # self.planet.mettre_a_jour_case(self.y, self.x, self.y, self.x, 0)
        self.planet.grille[self.y][self.x] = 0
        self.planet.requins.remove(self) 
    # Quand le requin meurt, il est retiré de la liste Requin   

planete_1 = Planet(50, 50)
# Initialiser la taille de la grille
planete_1.peupler_le_monde(1000,400)
# Initialiser le nombre de poissons et de requins
planete_1.simuler(5000)
# Lance la simulation pour une durée de x chronons

