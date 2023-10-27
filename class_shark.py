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