class Creature:
    def __init__(self, planet, x, y, energy=0):
        self.planet = planet
        self.x = x
        self.y = y
        self.energy = energy

    def move(self):
        pass