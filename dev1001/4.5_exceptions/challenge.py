'''
Build a “Dungeon Manager” that reads a JSON file of rooms, each with:
- room_id (int)
- num_players (int)
- difficulty (1-5)

Requirements:
1. Load dungeon.json.
2. For each room:
    - Use enter_room() to split loot.
    - Use spawn_enemies() to get enemy list.
    - Handle all I/O or data errors without crashing the loop.
3. Raise and catch a custom DungeonLoadError if JSON is malformed.
4. Log all errors to manager.log.
5. After processing, print summary: total rooms succeeded vs. failed.
'''

import json
import logging

logging.basicConfig(filename="manager.log", level=logging.INFO)

class DungeonError(Exception):
    pass

# TODO: define DungeonLoadError subclassing DungeonError

def enter_room(room_id, num_players):
    total_loot = 100
    return total_loot // num_players

def spawn_enemies(difficulty):
    if difficulty < 1 or difficulty > 5:
        raise ValueError("Invalid difficulty")
    return ["Goblin"] * difficulty

def process_dungeon(file_path):
    # TODO: load JSON, catch JSONDecodeError as dle and wrap in DungeonLoadError
    data = json.load(open(file_path))
    successes = fails = 0
    for room in data["rooms"]:
        try:
            loot = enter_room(room["room_id"], room["num_players"])
            enemies = spawn_enemies(room["difficulty"])
            print(f"Room {room['room_id']}: {loot} loot, {len(enemies)} enemies")
            successes += 1
        # TODO: catch and log specific and generic exceptions without stopping
        #       increment fails
    print(f"Succeeded: {successes}, Failed: {fails}")

if __name__ == "__main__":
    process_dungeon("dungeon.json")
