class Rock:
    icon = "🪨"

class Algae:
    icon = "🌿" 

    def initialize(self, num_rocks, num_algae):
        # Réinitialise la grille
        self.grid = [[None for _ in range(self.taille_de_la_grille)] for _ in range(self.taille_de_la_grille)]
        self.rock_positions = []
        self.algae_positions = []

        # Ajoute les nouveaux rochers et algues sans superposition
        for _ in range(num_rocks):
            while True:
                x, y = random.randint(0, self.taille_de_la_grille - 1), random.randint(0, self.taille_de_la_grille - 1)
                if self.grid[y][x] is None:
                    self.grid[y][x] = Rock()
                    self.rock_positions.append((x, y))
                    break

        for _ in range(num_algae):
            while True:
                x, y = random.randint(0, self.taille_de_la_grille - 1), random.randint(0, self.taille_de_la_grille - 1)
                if self.grid[y][x] is None:
                    self.grid[y][x] = Algae()
                    self.algae_positions.append((x, y))
                    break