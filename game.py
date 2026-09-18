from goblin import Goblin
from hero import Hero

ARENA_NAME = "The Closed Horshoe but Bigger and not as Skinny"

def battle(hero: Hero, enemies: list):
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

    battle(hero, goblins)

if __name__ == "__main__":
    main()
