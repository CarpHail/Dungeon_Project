def initialize(player_info):
    print("===== DUNGEON EXPLORER =====")
    print()
    name = input("Please enter your name: ")
    player_info = [name, 100, 0, 0]
    rooms = 0
    print(f"Welcome to the dungeon, {name}!")
    print()
    return player_info

def status(player_info, player_inventory):
    print("===== DUNGEON EXPLORER =====")
    print(f"Player: {player_info[0]}")
    print(f"Health: {player_info[1]}")
    print(f"Gold: {player_info[2]}")
    print(f"Rooms Explored: {player_info[3]}/10")
    print()

def main():
    player_info = []
    player_inventory = []
    
    print("=====DUNGEON EXPLORER=====")
    print()

    new_game = input("New Game? (y/n): ")
    if new_game.lower() == "y":
        player_info = initialize(player_info)

    while True:
        status(player_info, player_inventory)
        command = input("Enter your choice: ")
    
    

if __name__ == "__main__":
    main()
