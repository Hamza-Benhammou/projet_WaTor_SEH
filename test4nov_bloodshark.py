# import random
# import os
# import time
# import pygame
# import sys
# import mixer

# class Planet:
#     def __init__(self, largeur_de_la_grille, hauteur_de_la_grille):
#         self.largeur_de_la_grille = largeur_de_la_grille
#         self.hauteur_de_la_grille = hauteur_de_la_grille
#         self.grille = [[0 for case in range(self.largeur_de_la_grille)] for _ in range(self.hauteur_de_la_grille)]
#         self.poissons = []
#         self.requins = []
#         self.chronons = 0

#     def peupler_le_monde(self, nombre_poissons, nombre_requins):
#         self.poissons = [Poisson(self) for poisson in range(nombre_poissons)]
#         self.requins = [Requin(self) for requin in range(nombre_requins)]
#         # Cette méthode ajoute le nombre de poissons et de requins dans chaque liste vide.

#     def afficher_le_monde(self):
#         for ligne in self.grille:
#             print(*ligne)
#         print(f"\nPopulation de poissons: {len(self.poissons)} \nPopulation de requins: {len(self.requins)}\nNombre de chronons : {self.chronons}")
#         # A chaque chronon, cette méthode affiche l'état actuel du monde et sa population.

#     def verifer_case_vide(self, y, x):
#         return self.grille[int(y % self.hauteur_de_la_grille)][int(x % self.largeur_de_la_grille)] == 0
#     # Cette méthode vérifie si une case [y,x] est vide

#     def verifer_case_poisson(self, y, x):
#         return self.grille[int(y % self.hauteur_de_la_grille)][int(x % self.largeur_de_la_grille)] == '\U0001f41f'
#     # Cette méthode vérifie si une case [y,x] contient un poisson

#     def mettre_a_jour_case(self, y_initial, x_initial, y_nouveau, x_nouveau, valeur_poisson):
#         self.grille[(int(y_initial)) % int(self.hauteur_de_la_grille)][int(x_initial) % int(self.largeur_de_la_grille)] = 0
#         self.grille[int(y_nouveau) % int(self.hauteur_de_la_grille)][int(x_nouveau) % int(self.largeur_de_la_grille)] = valeur_poisson

#     def simuler(self, duree):
#         self.chronons = 0
#         for chronon in range(duree):
#             os.system('clear')
#             for requin in self.requins:
#                 requin.deplacement()
#             for poisson in self.poissons:
#                 poisson.deplacement() 
#             self.chronons += 1
#             self.afficher_le_monde()
#             time.sleep(.2)

#     # Cette méthode lance la simulation. duree = nombre de chronons

# class Poisson:
#     def __init__(self, planet):
#         self.x = random.choice(range(planet.largeur_de_la_grille))
#         self.y = random.choice(range(planet.hauteur_de_la_grille))
#         self.planet = planet
#         self.valeur_poisson = '\U0001f41f'
#         self.age = 0
#         self.temps_reproduction = 8
#         self.vitesse_x = 1
#         self.vitesse_y = 1

#     def choisir_deplacement_case_vide(self):
#         case_vide = []
#         if self.planet.verifer_case_vide(self.y + 1, self.x):
#             case_vide.append([(self.y + 1) % self.planet.hauteur_de_la_grille , self.x])

#         if self.planet.verifer_case_vide(self.y - 1, self.x):
#             case_vide.append([(self.y - 1) % self.planet.hauteur_de_la_grille, self.x])

#         if self.planet.verifer_case_vide(self.y, self.x + 1):
#             case_vide.append([self.y, (self.x + 1) % self.planet.largeur_de_la_grille])

#         if self.planet.verifer_case_vide(self.y, self.x - 1):
#             case_vide.append([self.y, (self.x - 1) % self.planet.largeur_de_la_grille])

#         if case_vide:
#             return case_vide
#         else:
#             return
#         # Cette méthode permet de scanner les 4 cases autour du poisson et ajoute les cases vides dans une liste
#         # return case_vide permet de récupérer la liste si elle contient des coordonnées quand on appelle la méthode


#     def deplacement(self, delta_time):
#        ##if self.choisir_deplacement_case_vide():
#             ##a = random.choice(self.choisir_deplacement_case_vide())
#             ##nouveau_y = a[0] ##+ self.vitesse_y * delta_time
#             ##nouveau_x = a[1] ##+ self.vitesse_x * delta_time
#             ##self.planet.grille[self.y][self.x] = 0

#         case_vide = self.choisir_deplacement_case_vide()
#         if case_vide:
#             nouveau_x, nouveau_y = random.choice(case_vide)
#             distance_x = nouveau_x - self.x
#             distance_y = nouveau_y - self.y

#             vitesse_deplacement = 0.1

#             deplacement_x = vitesse_deplacement * delta_time * distance_x
#             deplacement_y = vitesse_deplacement * delta_time * distance_y

#             # Mettez à jour la position actuelle
#             self.x += deplacement_x
#             self.y += deplacement_y

#             # Mettez à jour la grille pour refléter la nouvelle position
#             self.planet.mettre_a_jour_case(self.y - deplacement_y, self.x - deplacement_x, self.y, self.x, self.valeur_poisson)


#             if self.age == self.temps_reproduction:
#                 self.reproduction()
#                 self.age = 0
#             ##self.x = int(nouveau_x)% self.planet.largeur_de_la_grille
#             ##self.y = int(nouveau_y)%self.planet.hauteur_de_la_grille
#             ##self.planet.grille[self.y][self.x] = self.valeur_poisson

#         else:
#             return
#         self.age += 1

#         # Si la liste case_vide contient des coordonnées, le poisson se reproduit s'il a atteint l'age et se déplace

#     def reproduction(self):
#         new_poisson = Poisson(self.planet)
#         new_poisson.x = self.x
#         new_poisson.y = self.y
#         self.planet.poissons.append(new_poisson)
#         self.planet.grille[int(self.y)][int(self.x)] = self.valeur_poisson
#         # Quand un poisson se reproduit, le nouveau poisson récupère les coordoonées du parent et est ajouté à la liste Poisson

# class Requin(Poisson):
#     def __init__(self, planet):
#         super().__init__(planet)
#         self.valeur_poisson = '🦀'
#         self.starvation = 10
#         self.temps_reproduction = 40
#         self.vitesse_x = 1
#         self.vitesse_y =1

#     def choisir_deplacement_case_poisson(self):
#         case_poisson = []
#         if self.planet.verifer_case_poisson(self.y + 1, self.x):
#             case_poisson.append([(self.y + 1) % self.planet.hauteur_de_la_grille, self.x])

#         if self.planet.verifer_case_poisson(self.y - 1, self.x):
#             case_poisson.append([(self.y - 1) % self.planet.hauteur_de_la_grille, self.x])

#         if self.planet.verifer_case_poisson(self.y, self.x + 1):
#             case_poisson.append([self.y, (self.x + 1) % self.planet.largeur_de_la_grille])

#         if self.planet.verifer_case_poisson(self.y, self.x - 1):
#             case_poisson.append([self.y, (self.x - 1) % self.planet.largeur_de_la_grille])
#         return case_poisson
#         # Cette méthode permet de scanner les 4 cases autour du requin et ajoute les cases occupées par un poisson dans une liste
#         # return case_vide permet de récupérer la liste si elle contient des coordonnées quand on appelle la méthode

#     def choix_de_la_case(self):
#         casepoisson = self.choisir_deplacement_case_poisson()
#         casevide = self.choisir_deplacement_case_vide()
#         if casepoisson:
#             return casepoisson
#         elif casevide:
#             return casevide
#         # Le requin choisit en priorité une case occupée par un poisson, sinon il choisit les coordonnées d'une case vide
#         # Mais il ne se déplace pas encore

#     def deplacement(self, delta_time):
#         choix = self.choix_de_la_case()
#         if choix:
#             ##nouveau_y, nouveau_x = random.choice(choix)
#             ##a = random.choice(self.choisir_deplacement_case_vide())
#             ##nouveau_y = a[0] ##+ self.vitesse_y * delta_time
#             ##nouveau_x = a[1] ##+ self.vitesse_x * delta_time
#             ##nouveau_x = random.choice(self.choisir_deplacement_case_vide()) + self.vitesse_x * delta_time
#             ##nouveau_y = random.choice(self.choisir_deplacement_case_vide()) + self.vitesse_y * delta_time
        
#             nouveau_x, nouveau_y = random.choice(choix)
            
#             distance_x = nouveau_x - self.x
#             distance_y = nouveau_y - self.y

#             vitesse_deplacement = 0.1
            
#             deplacement_x = vitesse_deplacement * delta_time * distance_x
#             deplacement_y = vitesse_deplacement * delta_time * distance_y

#             self.x += deplacement_x
#             self.y += deplacement_y

#             self.planet.mettre_a_jour_case(self.y, self.x, nouveau_y, nouveau_x, self.valeur_poisson)

#             ##self.planet.grille[self.y][self.x] = 0
#             if self.age == self.temps_reproduction:
#                 self.reproduction()
#                 self.age = 0

#             ##self.x = int(nouveau_x) % self.planet.largeur_de_la_grille
#             ##self.y = int(nouveau_y) % self.planet.hauteur_de_la_grille
#             ##self.planet.grille[self.y][self.x] = self.valeur_poisson

#         else:
#             return
#         self.age += 1


#         poissons_sur_case = [poisson for poisson in self.planet.poissons if poisson.y == self.y and poisson.x == self.x]

#         if poissons_sur_case:
#             poisson = poissons_sur_case[0]
#             self.manger(poisson)

#         self.starvation -= 1
#         if self.starvation == 0:
#             self.mourir()

#         # Si le requin peut se déplacer, il se reproduit s'il a atteint l'age et se déplace sur une case poisson ou une case vide
#         # Si un requin se déplace sur un case poisson, ce poisson est ajouté à une liste et il est ensuite mangé.
#         # Le requin perd un point d'énergie, s'il atteint 0, il meurt


#     def manger(self, poisson):
#         self.planet.poissons.remove(poisson)
#         self.starvation += 3
#         # Le poisson mangé est retiré de la liste Poisson      
#         # Le requin regagne 3 points d'énergie

#     def reproduction(self):
#         new_requin = Requin(self.planet)
#         new_requin.y = self.y
#         new_requin.x = self.x
#         self.planet.requins.append(new_requin)
#         self.planet.grille[self.y][self.x] = self.valeur_poisson
#         # Quand un poisson se reproduit, le nouveau poisson récupère les coordoonées du parent et est ajouté à la liste Poisson

#     def mourir(self):
#         # self.planet.mettre_a_jour_case(self.y, self.x, self.y, self.x, 0)
#         self.planet.grille[int(self.y)][int(self.x)] = 0
#         self.planet.requins.remove(self)      
#         # Quand le requin meurt, il est retiré de la liste Requin




# class GraphicalDisplay(Planet):

#     def __init__(self, largeur_de_la_grille, hauteur_de_la_grille):
        
#         super().__init__(largeur_de_la_grille, hauteur_de_la_grille)
#         pygame.init()

#         musica = "bubbles_sound.mp3" 
#         pygame.mixer.music.load(musica)
#         pygame.mixer.music.play(-1)
#         #charge musique et tourne en boucle

#         self.screen = pygame.display.set_mode((400, 400))
#         pygame.display.set_caption("WATOR")

#         self.image_poisson = pygame.image.load('fish.jpg')
#         self.image_requin = pygame.image.load('shark.jpg')

#         vitesse_poisson = 1
#         vitess_requin = 1

#     def move (self, delta_time):
#         for poisson in self.poissons:
#             poisson.deplacement(delta_time)
#         for requin in self.requins:
#             requin.deplacement(delta_time)

#     def simuler(self, duree):
#         t = 0
#         running = True

#         clock = pygame.time.Clock()

#         while running:
#             for event in pygame.event.get():
#                 if event.type == pygame.QUIT:
#                     running = False

#             delta_time = clock.tick(60) / 1000.0
#             self.move(delta_time)

#             couleur_fond = (173, 216, 230) 
#             self.screen.fill(couleur_fond)
#             for y in range(self.hauteur_de_la_grille):
#                 for x in range(self.largeur_de_la_grille):
#                     if self.grille[y][x] == '\U0001f41f':
#                         self.screen.blit(self.image_poisson, (x * 40, y * 40)) 
#                     elif self.grille[y][x] == '🦀':
#                         self.screen.blit(self.image_requin, (x * 40, y * 40))  
#             for requin in self.requins:
#                 requin.deplacement(delta_time)
#             for poisson in self.poissons:
#                 poisson.deplacement(delta_time)

#             pygame.display.flip()

#             self.chronons += 1
#             self.afficher_le_monde()
#             time.sleep(0.5)
               

#             if self.chronons >= duree:
#                 running = False
#             time.sleep(0.5)

#         pygame.quit()
#         #boucle du jeu: definit le fond, et scanne la grille pour placer les poissons et les requins
#         #les deplacer et 

    

# class Blood(Requin):
#     def __init__(self, x,y):
#         pass



# #test terminal
# # planete_1 = Planet(20, 20)
# # planete_1.peupler_le_monde(1000, 300)
# # planete_1.simuler(10)

# #test pygame
# planete2= GraphicalDisplay(10, 10)
# planete2.peupler_le_monde(10, 3)
# planete2.simuler(20)




import random
import os
import time
import pygame

class Planet:
    def __init__(self, largeur_de_la_grille, hauteur_de_la_grille):
        self.largeur_de_la_grille = largeur_de_la_grille
        self.hauteur_de_la_grille = hauteur_de_la_grille
        self.grille = [[0 for case in range(self.largeur_de_la_grille)] for _ in range(self.hauteur_de_la_grille)]
        self.poissons = []
        self.requins = []
        self.chronons = 0

    def peupler_le_monde(self, nombre_poissons, nombre_requins):
        self.poissons = [Poisson(self) for poisson in range(nombre_poissons)]
        self.requins = [Requin(self) for requin in range(nombre_requins)]
        # Cette méthode ajoute le nombre de poissons et de requins dans chaque liste vide.

    def afficher_le_monde(self):
        for ligne in self.grille:
            print(*ligne)
        print(f"\nPopulation de poissons: {len(self.poissons)} \nPopulation de requins: {len(self.requins)}\nNombre de chronons : {self.chronons}")
        # A chaque chronon, cette méthode affiche l'état actuel du monde et sa population.

    def verifer_case_vide(self, y, x):
        return self.grille[int(y % self.hauteur_de_la_grille)][int(x % self.largeur_de_la_grille)] == 0
    # Cette méthode vérifie si une case [y,x] est vide

    def verifer_case_poisson(self, y, x):
        return self.grille[int(y % self.hauteur_de_la_grille)][int(x % self.largeur_de_la_grille)] == '\U0001f41f'
    # Cette méthode vérifie si une case [y,x] contient un poisson

    def mettre_a_jour_case(self, y_initial, x_initial, y_nouveau, x_nouveau, valeur_poisson):
        self.grille[(int(y_initial)) % int(self.hauteur_de_la_grille)][int(x_initial) % int(self.largeur_de_la_grille)] = 0
        self.grille[int(y_nouveau) % int(self.hauteur_de_la_grille)][int(x_nouveau) % int(self.largeur_de_la_grille)] = valeur_poisson

    def simuler(self, duree):
        self.chronons = 0
        for chronon in range(duree):
            os.system('clear')
            for requin in self.requins:
                requin.deplacement(1)
            for poisson in self.poissons:
                poisson.deplacement(1) 
            self.chronons += 1
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

    def deplacement(self, delta_time):
        case_vide = self.choisir_deplacement_case_vide()
        if case_vide:
            nouvel_x, nouvel_y = random.choice(case_vide)

            distance_x = nouvel_x - self.x
            distance_y = nouvel_y - self.y
            vitesse_deplacement = 0.1  # Ajustez cette valeur

            temps_deplacement_total = (abs(distance_x) + abs(distance_y)) / vitesse_deplacement

            self.nouveau_x = nouvel_x
            self.nouveau_y = nouvel_y
            self.temps_deplacement_total = temps_deplacement_total

            if self.age == self.temps_reproduction:
                self.reproduction()
                self.age = 0
        else:
            return
        self.age += 1

    def move(self, delta_time):
        if hasattr(self, 'nouveau_x') and hasattr(self, 'nouveau_y'):
            progression = min(1, delta_time / self.temps_deplacement_total)

            self.x = self.x + (self.nouveau_x - self.x) * progression
            self.y = self.y + (self.nouveau_y - self.y) * progression

            self.temps_deplacement_total -= delta_time

            if self.temps_deplacement_total <= 0:
                delattr(self, 'nouveau_x')
                delattr(self, 'nouveau_y')

        # ... Le reste du code de move reste inchangé
            vitesse_deplacement = 0.1

            deplacement_x = vitesse_deplacement * delta_time * distance_x
            deplacement_y = vitesse_deplacement * delta_time * distance_y

            # Mettez à jour la position actuelle
            self.x += deplacement_x
            self.y += deplacement_y

            # Mettez à jour la grille pour refléter la nouvelle position
            self.planet.mettre_a_jour_case(self.y - deplacement_y, self.x - deplacement_x, self.y, self.x, self.valeur_poisson)


            if self.age == self.temps_reproduction:
                self.reproduction()
                self.age = 0
            ##self.x = int(nouveau_x)% self.planet.largeur_de_la_grille
            ##self.y = int(nouveau_y)%self.planet.hauteur_de_la_grille
            ##self.planet.grille[self.y][self.x] = self.valeur_poisson

        else:
            return
        self.age += 1


    def reproduction(self):
        new_poisson = Poisson(self.planet)
        new_poisson.x = self.x
        new_poisson.y = self.y
        self.planet.poissons.append(new_poisson)
        self.planet.grille[int(self.y)][int(self.x)] = self.valeur_poisson
        # Quand un poisson se reproduit, le nouveau poisson récupère les coordoonées du parent et est ajouté à la liste Poisson

class Requin(Poisson):
    def __init__(self, planet):
        super().__init__(planet)
        self.valeur_poisson = '🦀'
        self.starvation = 10
        self.temps_reproduction = 40
        self.vitesse_x = 1
        self.vitesse_y =1


    # ... (votre code de choisir_deplacement_case_poisson, choix_de_la_case, et deplacement reste inchangé)
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




    def deplacement(self, delta_time):
        choix = self.choix_de_la_case()
        if choix:
            nouvel_x, nouvel_y = random.choice(choix)

            distance_x = nouvel_x - self.x
            distance_y = nouvel_y - self.y
            vitesse_deplacement = 0.1

            temps_deplacement_total = (abs(distance_x) + abs(distance_y)) / vitesse_deplacement

            self.nouveau_x = nouvel_x
            self.nouveau_y = nouvel_y
            self.temps_deplacement_total = temps_deplacement_total

            if self.age == self.temps_reproduction:
                self.reproduction()
                self.age = 0

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
        self.planet.grille[int(self.y)][int(self.x)] = 0
        self.planet.requins.remove(self)      
        # Quand le requin meurt, il est retiré de la liste Requin


class GraphicalDisplay(Planet):
    def __init__(self, largeur_de_la_grille, hauteur_de_la_grille):
        super().__init__(largeur_de_la_grille, hauteur_de_la_grille)
        pygame.init()
        super().__init__(largeur_de_la_grille, hauteur_de_la_grille)


        musica = "bubbles_sound.mp3" 
        pygame.mixer.music.load(musica)
        pygame.mixer.music.play(-1)
        #charge musique et tourne en boucle

        self.screen = pygame.display.set_mode((400, 400))
        pygame.display.set_caption("WATOR")

        self.image_poisson = pygame.image.load('fish.jpg')
        self.image_requin = pygame.image.load('shark.jpg')

        vitesse_poisson = 1
        vitess_requin = 1


    def move(self, delta_time):
        for poisson in self.poissons:
            poisson.move(delta_time)
        for requin in self.requins:
            requin.move(delta_time)

    def simuler(self, duree):
        t = 0
        running = True
        clock = pygame.time.Clock()

        while running:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    running = False

            delta_time = clock.tick(60) / 1000.0
            self.move(delta_time)

            couleur_fond = (173, 216, 230)
            self.screen.fill(couleur_fond)
            for y in range(self.hauteur_de_la_grille):
                for x in range(self.largeur_de_la_grille):
                    if self.grille[y][x] == '\U0001f41f':
                        self.screen.blit(self.image_poisson, (x * 40, y * 40))
                    elif self.grille[y][x] == '🦀':
                        self.screen.blit(self.image_requin, (x * 40, y * 40))
            for requin in self.requins:
                requin.move(delta_time)
            for poisson in self.poissons:
                poisson.move(delta_time)

            pygame.display.flip()

            self.chronons += 1
            self.afficher_le_monde()
            time.sleep(0.5)

            if self.chronons >= duree:
                running = False
            time.sleep(0.5)

        pygame.quit()

# Le reste de votre code, y compris la classe Blood, reste inchangé

# test pygame
#planete2 = GraphicalDisplay(10, 10)
#planete2.peupler_le_monde(10, 3)
#planete2.simuler(20)

planete = Planet(10, 10)
planete.peupler_le_monde(10, 3)

# Simulez le monde pendant 20 chronons
planete.simuler(20)


