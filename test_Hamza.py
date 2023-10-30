import random

class Planet:
    def __init__(self, largeur_de_la_grille, hauteur_de_la_grille):
        self.largeur_de_la_grille = largeur_de_la_grille
        self.hauteur_de_la_grille = hauteur_de_la_grille
        self.grid = [[None for _ in range(self.largeur_de_la_grille)] for _ in range(self.hauteur_de_la_grille)]

    def is_valid_position(self, x, y):
        return 0 <= x < self.largeur_de_la_grille and 0 <= y < self.hauteur_de_la_grille

    def get_empty_positions(self):
        empty_positions = []
        for y in range(self.hauteur_de_la_grille):
            for x in range(self.largeur_de_la_grille):
                if self.grid[y][x] is None:
                    empty_positions.append((x, y))
        return empty_positions

    def display(self):
        for ligne in self.grid:
            for case in ligne:
                if case is None:
                    print(" ", end=" ")
                else:
                    print(case.icon, end=" ")
            print()

class Creature:
    def __init__(self, planet, x, y, energy=0):
        self.planet = planet
        self.x = x
        self.y = y
        self.energy = energy

    def move(self):
        pass

class Fish(Creature):
    icon = "🐟"

    def move(self):
        directions = [(0, 1), (0, -1), (1, 0), (-1, 0)]
        random.shuffle(directions)

        for dx, dy in directions:
            new_x = self.x + dx
            new_y = self.y + dy

            if self.planet.is_valid_position(new_x, new_y) and self.planet.grid[new_y][new_x] is None:
                self.planet.grid[self.y][self.x] = None
                self.x = new_x
                self.y = new_y
                self.planet.grid[new_y][new_x] = self
                break

class Shark(Creature):
    icon = "🦈"

    def __init__(self, planet, x, y, energy):
        super().__init__(planet, x, y, energy)
        self.starvation = 0

    class Shark(Creature):
        icon = "🦈"

    def move(self):
        directions = [(0, 1), (0, -1), (1, 0), (-1, 0)]
        random.shuffle(directions)

        for dx, dy in directions:
            new_x = self.x + dx
            new_y = self.y + dy

            if self.planet.is_valid_position(new_x, new_y):
                if self.planet.grid[new_y][new_x] is None:
                    self.planet.grid[self.y][self.x] = None
                    self.x = new_x
                    self.y = new_y
                    self.planet.grid[new_y][new_x] = self
                    self.energy -= 1  # Dépense d'énergie pour se déplacer

                elif isinstance(self.planet.grid[new_y][new_x], Fish):
                    # Le requin a mangé un poisson
                    self.energy += 4
                    self.starvation = 0
                    self.planet.grid[new_y][new_x] = None

                if self.energy <= 0:
                    # Le requin meurt de faim
                    self.planet.grid[self.y][self.x] = None
                    self.starvation += 1
                    if self.starvation >= 3:
                        # Reproduction si la faim est de 3 chronons
                        empty_positions = self.planet.get_empty_positions()
                        if empty_positions:
                            x, y = random.choice(empty_positions)
                            self.planet.grid[y][x] = Shark(self.planet, x, y, self.energy)

                    break


def main():
    
    largeur_de_la_grille = 10
    hauteur_de_la_grille = 10

    planete = Planet(largeur_de_la_grille, hauteur_de_la_grille)

    poissons = [Fish(planete, random.randint(0, largeur_de_la_grille - 1), random.randint(0, hauteur_de_la_grille - 1)) for _ in range(10)]
    requins = [Shark(planete, random.randint(0, largeur_de_la_grille - 1), random.randint(0, hauteur_de_la_grille - 1), 5) for _ in range(5)]

    num_steps = 20
    step = 0

    while step < num_steps:
        planete.display()
        for poisson in poissons:
            poisson.move()
        for requin in requins:
            requin.move()
        step += 1

if __name__ == "__main__":
    main()

