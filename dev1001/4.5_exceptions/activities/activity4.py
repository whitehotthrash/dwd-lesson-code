class Player:
    def __init__(self, name, health, level):
        if not name:
            raise ValueError("Player must have a name.")
        if health < 0:
            raise ValueError("Health cannot be negative.")
        # TODO: if level < 1, raise ValueError("Level must be at least 1")
        self.name = name
        self.health = health
        self.level = level

def main():
    try:
        p = Player("Rogue", 80, 0)
    except ValueError as ve:
        print(f"Error: {ve}")
