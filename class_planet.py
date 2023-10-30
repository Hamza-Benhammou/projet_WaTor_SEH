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