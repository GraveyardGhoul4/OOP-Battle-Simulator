from goblin import Goblin


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


if __name__ == "__main__":
    main()
