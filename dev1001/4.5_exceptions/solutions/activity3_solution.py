import logging
logging.basicConfig(filename="game.log", level=logging.INFO)

def load_level_data(path):
    with open(path) as f:
        return f.read()

def main():
    level_file = input("Level filename? ")
    try:
        data = load_level_data(level_file)
        print("Level loaded.")
    except FileNotFoundError as fnf:
        logging.error(f"Missing file: {fnf.args}")
        print("Level file not found.")
    except Exception as e:
        logging.error(f"Error loading level: {type(e).__name__}, args={e.args}")
        print("Unexpected error.")
    finally:
        print("Load attempt complete.")

    
