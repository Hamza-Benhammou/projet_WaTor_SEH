class Fish(Creature): # Normal qu'il soit souligné il censé hériter de créature situé 
                        # sur un autre script
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