import json
import logging

logging.basicConfig(filename="manager.log", level=logging.INFO)

class DungeonError(Exception):
    pass

class DungeonLoadError(DungeonError):
    """Raised when dungeon JSON is invalid."""

def enter_room(room_id, num_players):
    total_loot = 100
    return total_loot // num_players

def spawn_enemies(difficulty):
    if difficulty < 1 or difficulty > 5:
        raise ValueError("Invalid difficulty")
    return ["Goblin"] * difficulty

def process_dungeon(file_path):
    try:
        with open(file_path) as f:
            data = json.load(f)
    except json.JSONDecodeError as dle:
        raise DungeonLoadError(f"Bad JSON: {dle}") from dle
    except FileNotFoundError as fnf:
        logging.error(f"File missing: {fnf}")
        return

    successes = fails = 0
    for room in data.get("rooms", []):
        try:
            loot = enter_room(room["room_id"], room["num_players"])
            enemies = spawn_enemies(room["difficulty"])
            print(f"Room {room['room_id']}: {loot} loot, {len(enemies)} enemies")
            successes += 1
        except KeyError as ke:
            logging.error(f"Missing key {ke} in room {room}")
            print(f"Skipping room due to missing data.")
            fails += 1
        except DungeonError as de:
            logging.error(f"Dungeon error: {de}")
            print(f"Error in room: {de}")
            fails += 1
        except Exception as e:
            logging.error(f"Unexpected error {type(e).__name__}: {e}")
            print("Unexpected error—skipping room.")
            fails += 1

    print(f"Succeeded: {successes}, Failed: {fails}")

if __name__ == "__main__":
    process_dungeon("dungeon.json")
