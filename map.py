from dataclasses import dataclass, field
from typing import Optional, List

@dataclass
class Character:
    symbol: str  # symbol character example for player = [P]
    location: List[List[int]] = field(default_factory=lambda: [[0, 0]])
    current_location : Optional[List[List[int]]] = field(default_factory=lambda: [[0, 0]])
    next_location : Optional[List[List[int]]] = field(default_factory=lambda: [[0, 0]])
    previous_location : Optional[List[List[int]]] = field(default_factory=lambda: [[0, 0]])


class Map:

    map = None
    rows = None
    cols = None

    def __init__(self,rows, cols):
        self.rows = rows
        self.cols = cols
        self.create_map_content()


    def assign_content(self, coordinates, symbol):

        for coordinate in coordinates:
            x = coordinate[0]
            y = coordinate[1]
            self.map[x][y] = symbol


    def create_map_content(self):

        # by default all coodinate will show as [ ]
        map = [["[ ]" for _ in range(self.cols)] for _ in range(self.rows)]

        # #assign blank space or lines
        for i, row in enumerate(map):
            for j, col in enumerate(row):

                if (i == len(map)-1 or j == len(row)-1):  # tackle last coodinate
                    map[i][j] = ""
                elif (i%2 != 0):
                    map[i][j]= "   "
                elif (j%2 !=0):
                    map[i][j]= "   "

        self.map = map

    def display_map(self):
        for rows in self.map:
            line = ""
            for col in rows:
                line = line + col
            print(line)

    def move(self, direction):

        x = player.current_location[0][0]
        y = player.current_location[0][1]

        if (direction == 'DOWN'):
            print("direction is down" )

            player.next_location[0][0] = x + 2
            player.next_location[0][1] = y

        elif (direction == 'RIGHT'):
            print("direction is right" )

            x = player.current_location[0][0]
            y = player.current_location[0][1]

            player.next_location[0][0] = x
            player.next_location[0][1] = y + 2

        elif (direction == 'LEFT'):
            print("direction is left" )

            x = player.current_location[0][0]
            y = player.current_location[0][1]

            player.next_location[0][0] = x
            player.next_location[0][1] = y - 2

        elif (direction == 'UP'):
            print("direction is up" )

            x = player.current_location[0][0]
            y = player.current_location[0][1]

            player.next_location[0][0] = x - 2
            player.next_location[0][1] = y

        player.previous_location[0][0] = x
        player.previous_location[0][1] = y

        player.current_location = player.next_location[:]

        # print(f"previous : {player.previous_location}")
        # print(f"current: {player.current_location}")
        # print(f"next : {player.next_location}")


# --------------------- Program start from here ----------------------------------------------------

#define player initial location and symbol to display in UI
player = Character( location =[[0,0]],symbol='[P]')
player.current_location = player.location.copy()

#define exit initial location and symbol to display in UI
exit = Character(location =[[8,8]], symbol='[E]' )
trace = Character(location =[[0,2],[2,2],[4,2]], symbol='[X]' )
vertical_path = Character(location =[[1,0],[1,2]], symbol=' | ' )
horizontal_path = Character(location =[[2,1],[4,1]], symbol=' - ' )
wall_tiles = Character(location =[[4,2],[6,2],[8,2]], symbol=' # ' )

room_map = Map(20, 20)
room_map.assign_content( player.location,player.symbol)  #enum.player.value()
room_map.assign_content(exit.location, exit.symbol)
room_map.assign_content(trace.location, trace.symbol)
room_map.assign_content(vertical_path.location, vertical_path.symbol)
room_map.assign_content(horizontal_path.location, horizontal_path.symbol)
room_map.assign_content(wall_tiles.location, wall_tiles.symbol)

print("Welcome to the interactive map game!")
print("Use 'UP', 'DOWN', 'RIGHT', 'LEFT' to move, and 'Q' to exit.")
while True:
    # Display the current map
    room_map.display_map()
    # Get the player's move
    direction = input("Enter your move: ").upper()
    if direction == "Q":
        print("Thanks for playing!")
        break
    elif direction in ["UP", "DOWN", "RIGHT", "LEFT"]:
        room_map.move(direction)
        room_map.assign_content(player.next_location, player.symbol)
        room_map.assign_content(player.previous_location,trace.symbol)
    else:
        print("Invalid command. Use 'UP', 'DOWN', 'RIGHT', 'LEFT' to move, and 'Q'.")