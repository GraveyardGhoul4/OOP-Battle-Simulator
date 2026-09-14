from goblin import Goblin
from hero import Hero

ARENA_NAME = "The Closed Horshoe but Bigger and not as Skinny"


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

    hero = Hero("Jerry", "Melee", 25, 10)

    print(f"{hero.name} enters the arena with {hero.health} health. Hero class is {hero.heroClass}. Hero defense is {hero.defense}. Hero critical chance is {hero.critChance}%.")

    heroAttack = hero.Attack()

    goblin.take_damage(heroAttack)

    if goblin.is_alive:
        goblinAttack = goblin.attack()
        hero.TakeDamage(goblinAttack)

if __name__ == "__main__":
    main()
