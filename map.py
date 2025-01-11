from enum import Enum

class Symbol(Enum):
    PLAYER = '[P]'
    WALL = '[#]'
    EXIT = '[E]'
    TRACE = '[X]'
    VERTICAL_PATH = ' | '
    HORIZONTAL_PATH = ' - '

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

        if (direction == 'S'):
            print("direction is down" )
            self.assign_content([(2,0)], Symbol.PLAYER.value)
            self.assign_content([(0,0)], Symbol.TRACE.value)

            # (0,0)  --> (2,0)

# --------------------- Program start from here ----------------------------------------------------

player = [(0,0)]
exit = [(8,8)]
trace = [(0,2),(2,2),(4,2)]
vertical_path = [(1,0),(1,2)]
horizontal_path = [(2,1)]
wall_tiles = [(4,2),(6,2),(8,2)]

room_map = Map(10, 10)
room_map.assign_content( player, Symbol.PLAYER.value)
room_map.assign_content(exit, Symbol.EXIT.value)
room_map.assign_content(trace, Symbol.TRACE.value)
room_map.assign_content(vertical_path, Symbol.VERTICAL_PATH.value)
room_map.assign_content(horizontal_path, Symbol.HORIZONTAL_PATH.value)
room_map.assign_content(wall_tiles, Symbol.WALL.value)

print("Welcome to the interactive map game!")
print("Use 'N', 'S', 'E', 'W' to move, and 'Q' to exit.")
while True:
    # Display the current map
    room_map.display_map()
    # Get the player's move
    direction = input("Enter your move: ").upper()
    if direction == "Q":
        print("Thanks for playing!")
        break
    elif direction in ["N", "S", "E", "W"]:
        print("move to " + direction )
        room_map.move(direction)
    else:
        print("Invalid command. Use 'N', 'S', 'E', 'W' to move, and 'Q'.")