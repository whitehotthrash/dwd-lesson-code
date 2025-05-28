def spawn_enemies(difficulty):
    if difficulty < 1 or difficulty > 5:
        raise ValueError("Difficulty out of range!")
    return ["Orc"] * difficulty

def main():
    lvl = input("Difficulty (1-5)? ")
    try:
        enemies = spawn_enemies(int(lvl))
        print(f"Spawned {len(enemies)} enemies.")
    except ValueError:
        print("Spawning 1 Training Dummy.")
        enemies = ["Training Dummy"]
    except Exception:
        print("Spawn failed completely.")
        return
    print("Battle starts!")
