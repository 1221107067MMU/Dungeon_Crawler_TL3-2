# Define the game map
game_map = [
    ['[Entrance]', '---', '[Hallway]', '---', '[Armory]'],
    ['|', '', '|', '', ''],
    ['[Library]', '', '[Trap Room]', '---', '[Treasure Room]'],
    ['|', '', '', '', ''],
    ['[Hidden Room]', '', '', '', '']
]

# Player starting position
player_position = [0, 0]  # Start at [Entrance]

# Function to display the map with the player's position
def display_map(game_map, player_pos):
    for row_index, row in enumerate(game_map):
        for col_index, cell in enumerate(row):
            # Highlight the player's current position
            if [row_index, col_index] == player_pos:
                print(f"[*{cell if cell else ' '}*]", end="")
            else:
                print(f"{cell if cell else '   '}", end="")
        print()  # Move to the next line

# Function to move the player
def move_player(direction, player_pos):
    row, col = player_pos
    if direction == "up" and row > 0 and game_map[row - 1][col] in ['|', '[Library]', '[Hidden Room]']:
        player_pos[0] -= 2  # Move up
    elif direction == "down" and row < len(game_map) - 1 and game_map[row + 1][col] in ['|', '[Library]', '[Hidden Room]']:
        player_pos[0] += 2  # Move down
    elif direction == "left" and col > 0 and game_map[row][col - 1] in ['---', '[Hallway]', '[Trap Room]', '[Treasure Room]']:
        player_pos[1] -= 2  # Move left
    elif direction == "right" and col < len(game_map[row]) - 1 and game_map[row][col + 1] in ['---', '[Hallway]', '[Trap Room]', '[Treasure Room]']:
        player_pos[1] += 2  # Move right
    else:
        print("You can't move in that direction!")

# Game loop
def play_game():
    print("Welcome to the interactive map game!")
    print("Use 'up', 'down', 'left', 'right' to move, and 'quit' to exit.")
    while True:
        # Display the current map
        display_map(game_map, player_position)
        # Get the player's move
        move = input("Enter your move: ").lower()
        if move == "quit":
            print("Thanks for playing!")
            break
        elif move in ["up", "down", "left", "right"]:
            move_player(move, player_position)
        else:
            print("Invalid command. Use 'up', 'down', 'left', 'right', or 'quit'.")

# Start the game
play_game()
