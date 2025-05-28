def enter_room(room_number, num_players):
    total_loot = 100
    loot_per_player = total_loot // num_players
    print(f"Each player receives {loot_per_player} gold coins.")

def main():
    room = input("Room number? ")
    players = input("Number of players? ")
    # TODO: wrap enter_room in try/except
    #       on error, print "Default loot: 10 coins each."
    #       then continue.
    enter_room(int(room), int(players))
    print("End of turn.")
    
if __name__ == "__main__":
    main()
