from enemy import Enemy
from hero import Hero
import random

class Boss(Enemy):
    def __init__(self, name, health, attackPower): 
        super().__init__(name, health)
        self.attackPower = attackPower

    def attack(self):
            """Return a random amount of damage."""
            return random.randint(1, self.attack_power * 2)

    def StealHealth(self, hero: Hero):
        health = random.randint(1,round(hero.health/4))
        hero.health -= health
        self.health += health
        print(f"{self.name} steals {health} health from {hero.name}. {self.health} health remaining")