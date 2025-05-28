def spawn_enemies(difficulty):
    if difficulty < 1 or difficulty > 5:
        raise ValueError("Difficulty out of range!")
    return ["Orc"] * difficulty

def main():
    lvl = input("Difficulty (1–5)? ")
    try:
        enemies = spawn_enemies(int(lvl))
        print(f"Spawned {len(enemies)} enemies.")
    # TODO: catch ValueError and other Exceptions
    #       ValueError → spawn dummy
    #       other → print failure
    # then always print "Battle starts!"
    
    print("Battle starts!")
