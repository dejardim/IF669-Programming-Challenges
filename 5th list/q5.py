"""21.1L5Q5 - Corre Berg, lá vem os Nazgûl"""

has_exit: int = 0


def show_map(maze: list):
    """Print maze and only that."""

    for line in maze:
        print("".join(line))


def route(maze, y, x):
    """MacGyver function to try find the exit route."""

    # Const variables
    WALL: str = "#"
    PATH: str = "."
    EXIT: str = "O"

    # dangerous but it helps
    # (doc): has_exit is a summation of zeros (exit not found) and ones (exit found).
    global has_exit

    # Base case (Check out range)
    if y > len(maze)-1 or y < 0 or x < 0 or x > len(maze)-1:
        return False

    # Questionable const variable
    WALK: str = maze[y][x]

    # Base case
    if WALK == WALL:
        return False
    if WALK == PATH or WALK == EXIT:
        return True

    # Define UP, DOWN, LEFT, RIGHT const vars (because move can not be locate out range)
    if y-1 >= 0:
        UP: str = maze[y - 1][x]
    else:
        UP = ""

    if y+1 <= len(maze)-1:
        DOWN: str = maze[y + 1][x]
    else:
        DOWN = ""

    if x-1 >= 0:
        LEFT: str = maze[y][x - 1]
    else:
        LEFT = ""

    if x+1 <= len(maze)-1:
        RIGHT: str = maze[y][x + 1]
    else:
        RIGHT = ""

    # Like a Base case
    if UP == EXIT:
        maze[y-1][x] = "F"
        show_map(maze)
        print("Por aqui meus amigos vamos pelo Norte\n")
        has_exit += 1
    elif DOWN == EXIT:
        maze[y+1][x] = "F"
        show_map(maze)
        print("Por aqui meus amigos vamos pelo Sul\n")
        has_exit += 1
    elif LEFT == EXIT:
        maze[y][x-1] = "F"
        show_map(maze)
        print("Por aqui meus amigos vamos pelo Oeste\n")
        has_exit += 1
    elif RIGHT == EXIT:
        maze[y][x+1] = "F"
        show_map(maze)
        print("Por aqui meus amigos vamos pelo Leste\n")
        has_exit += 1

    # Here is where discreet math shines and Anjolina can't see
    if (not UP == "F" and route(maze, y-1, x)) and (not DOWN == "F" and route(maze, y+1, x)) and\
            (not LEFT == "F" and route(maze, y, x-1)) and (not RIGHT == "F" and route(maze, y, x+1)):
        maze[y+1][x] = "F"
        show_map(maze)
        print("Por aqui meus amigos vamos pelo Sul\n")
        route(maze, y+1, x)

    # C(4,2) = 4! / ((4 - 2)! * 2!) = 6 , then we have 6 conditionals for bifurcations:

    elif (not UP == "F" and route(maze, y-1, x)) and (not DOWN == "F" and route(maze, y+1, x)):  # up and down
        maze[y+1][x] = "F"
        show_map(maze)
        print("Por aqui meus amigos vamos pelo Sul\n")
        route(maze, y+1, x)
    elif (not UP == "F" and route(maze, y-1, x)) and (not LEFT == "F" and route(maze, y, x-1)):  # up and left
        maze[y-1][x] = "F"
        show_map(maze)
        print("Por aqui meus amigos vamos pelo Norte\n")
        route(maze, y-1, x)
    elif (not UP == "F" and route(maze, y-1, x)) and (not RIGHT == "F" and route(maze, y, x+1)):  # up and right
        maze[y][x+1] = "F"
        show_map(maze)
        print("Por aqui meus amigos vamos pelo Leste\n")
        route(maze, y, x+1)

    elif (not DOWN == "F" and route(maze, y+1, x)) and (not LEFT == "F" and route(maze, y, x-1)):  # down and left
        maze[y+1][x] = "F"
        show_map(maze)
        print("Por aqui meus amigos vamos pelo Sul\n")
        route(maze, y+1, x)
    elif (not DOWN == "F" and route(maze, y+1, x)) and (not RIGHT == "F" and route(maze, y, x+1)):  # down and right
        maze[y+1][x] = "F"
        show_map(maze)
        print("Por aqui meus amigos vamos pelo Sul\n")
        route(maze, y+1, x)

    elif (not LEFT == "F" and route(maze, y, x-1)) and (not RIGHT == "F" and route(maze, y, x+1)):  # left and right
        maze[y][x+1] = "F"
        show_map(maze)
        print("Por aqui meus amigos vamos pelo Leste\n")
        route(maze, y, x+1)

    # Now we are left with the simple movements

    elif not UP == "F" and route(maze, y - 1, x):
        maze[y-1][x] = "F"
        show_map(maze)
        print("Por aqui meus amigos vamos pelo Norte\n")
        route(maze, y-1, x)
    elif not DOWN == "F" and route(maze, y+1, x):
        maze[y+1][x] = "F"
        show_map(maze)
        print("Por aqui meus amigos vamos pelo Sul\n")
        route(maze, y+1, x)
    elif not LEFT == "F" and route(maze, y, x-1):
        maze[y][x-1] = "F"
        show_map(maze)
        print("Por aqui meus amigos vamos pelo Oeste\n")
        route(maze, y, x-1)
    elif not RIGHT == "F" and route(maze, y, x+1):
        maze[y][x+1] = "F"
        show_map(maze)
        print("Por aqui meus amigos vamos pelo Leste\n")
        route(maze, y, x+1)

    # I don't think I need that
    has_exit += 0


# Input maze dimension
dimension: int = int(input())

# Input coordinates of Frodo&friends
coord1: int = int(input())  # y
coord2: int = int(input())  # x

# Input each line of maze map
maze_map = [list(input()) for i in range(dimension)]

# Try to find the exit and print each step
route(maze_map, coord1, coord2)

# Final Output 
if has_exit:
    show_map(maze_map)
    print("Conseguimos!!")
else:
    print("Amigos a jornada foi incrível, porém ela acaba por aqui...")
