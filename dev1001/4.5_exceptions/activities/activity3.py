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
    # TODO: catch FileNotFoundError as fnf
    #       log "Missing file: <args>" and print user-friendly message
    # catch any other Exception as e
    #       log full exception
    # finally always print "Load attempt complete."
    
