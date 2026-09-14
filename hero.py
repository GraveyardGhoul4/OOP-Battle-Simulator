import random

class Hero:
    """The hero blueprint will be implemented later in the project."""

    def __init__(self, name, heroClass, critChance, defense):
            self.name = name
            self.health = 125
            self.attack_power = 20
            self.heroClass = heroClass
            self.critChance = critChance
            self.defense = defense
    
    def Attack(self):
        if random.randint(self.critChance, 100) == 100:
            return random.randint(1, self.attack_power) * 2
        else:
            return random.randint(1, self.attack_power)
    
    def TakeDamage(self, damage):
        damage -= round(self.defense * 0.5)
        self.health = max(0, self.health-damage)
        print(f"{self.name} took {damage} damage. {self.health} health remaining.")

    def IsAlive(self):
        return self.health > 0