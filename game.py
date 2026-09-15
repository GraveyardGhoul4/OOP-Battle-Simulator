from goblin import Goblin
from hero import Hero

ARENA_NAME = "The Closed Horshoe but Bigger and not as Skinny"

def battle(hero: Hero, enemy: Goblin):
    while hero.IsAlive() and enemy.is_alive():
        heroDamage = hero.Attack()
        enemy.take_damage(heroDamage)

        if enemy.is_alive():
            enemyDamage = enemy.attack()
            hero.TakeDamage(enemyDamage)

    if hero.IsAlive():
        print(f"{hero.name} Wins!")
    else:
        print(f"{enemy.name} Wins!")

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

    battle(hero, goblin)

if __name__ == "__main__":
    main()
