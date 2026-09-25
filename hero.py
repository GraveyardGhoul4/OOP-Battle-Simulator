import random

class Hero:
    """The hero blueprint will be implemented later in the project."""

    def __init__(self, name, heroClass, baseStrength, critChance, dodgeChance, defense):
            self.name = name
            self.health = 125
            self.attack_power = 20
            self.heroClass = heroClass
            self.baseStrength = baseStrength
            self.critChance = critChance
            self.dodgeChance = dodgeChance
            self.defense = defense
    
    def Attack(self):
        if random.randint(self.critChance, 100) == 100:
            print("Critical Hit")
            return random.randint(self.baseStrength, self.attack_power) * 2
        else:
            return random.randint(self.baseStrength, self.attack_power)
    
    def TakeDamage(self, damage):
        if random.randint(self.dodgeChance, 100) == 100:
            damage=0
            print("Dodges")
        else:    
            damage = max(0,damage-round(self.defense * 0.5))

        self.health = max(0, self.health-damage)
        print(f"{self.name} took {damage} damage. {self.health} health remaining.")

    def IsAlive(self):
        alive = self.health > 0
        if not alive:
            print(f"{self.name} has been defeated")
        return alive

    def Heal(self, amount):
        self.health += amount