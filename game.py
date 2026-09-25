from goblin import Goblin
from boss import Boss
from hero import Hero
import random

ARENA_NAME = "The Closed Horshoe but Bigger and not as Skinny"

def battleEnemies(hero: Hero, enemies: list):
    while hero.IsAlive() and len(enemies) > 0:
        length = len(enemies)
        heroDamage = hero.Attack()
        enemies[length-1].take_damage(heroDamage)
        if enemies[length-1].is_alive():
            enemyDamage = enemies[length-1].attack()
            hero.TakeDamage(enemyDamage)
        else:
            print(f"{enemies[length-1].name} has been defeated")
            enemies.pop()

def battleBoss(hero: Hero, boss: Boss):
    while hero.IsAlive() and boss.is_alive():
        heroDamage = hero.Attack()
        boss.take_damage(heroDamage)
        if boss.is_alive():
            if random.randint(1, 5) == 5:
                boss.StealHealth(hero)
            else:
                bossDamage = boss.attack()
                hero.TakeDamage(bossDamage)
        else:
            print(f"{boss.name} has been defeated")

def main():
    """Open the arena and introduce its first opponent."""
    print(f"Welcome to {ARENA_NAME}!")
    print("༼ ᓄºل͟º ༽ᓄ   ᕦ(ò_óˇ)ᕤ")
    print("The gates are opening...")

    goblin = Goblin("Hayes Harris")

    print(f"{goblin.name} enters the arena with {goblin.health} health.")

    newGoblin = Goblin("Scribble")
    
    print(f"{newGoblin.name} enters the arena with {newGoblin.health} health.")

    print("But no hero has answered the call... yet.")

    hero = Hero("Jerry", "Melee", 5, 25, 5, 2)

    print(f"{hero.name} enters the arena with {hero.health} health. Hero class is {hero.heroClass}. Hero defense is {hero.defense}. Hero critical chance is {hero.critChance}%.")

    goblins = [goblin, newGoblin]

    battleEnemies(hero, goblins)

    boss = Boss("Big Bad Boss", 175, 20)

    hero.Heal(100)
    
    battleBoss(hero, boss)
    

if __name__ == "__main__":
    main()
