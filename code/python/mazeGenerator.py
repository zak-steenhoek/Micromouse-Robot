# This program generates a randomized maze using the DFS algorithm
from tkinter import mainloop
import micromouse as mm
from micromouse import Micromouse
import turtle
from sys import argv

# constants
size = 32
maze_size = 8
offset = 16


# Get the wall data from encoded number given in input
def parse_walls(maze, x, y) -> list:
    walls = []
    val = maze[y][x]

    for i in range(4):
        walls.insert(0, val % 2)  # This bit is 1 if there is no wall in that direction
        val >>= 1

    return walls


class MazeDrawer(turtle.Pen):

    def draw_walls(self, maze) -> None:
        for y in range(maze_size):
            for x in range(maze_size):
                self.pu()
                self.setpos((x - (maze_size / 2)) * size, ((maze_size / 2) - y) * size)
                self.seth(0)
                walls = parse_walls(maze, x, y)

                for wall in walls:
                    if wall == 1:
                        self.pu()
                    else:
                        self.pd()
                    self.forward(size)
                    self.right(90)
        self.pu()


def draw(filename: str, start, target) -> None:
    # read the maze and create the maze
    with open(filename) as f:
        data = f.readlines()

    maze = []
    for line in data:
        l = [int(x) for x in line.split(",")]
        maze.append(l)

    global maze_size
    maze_size = len(maze)

    # create the drawer and draw the maze
    drawer = MazeDrawer()
    drawer.speed(0)
    drawer.hideturtle()
    drawer.draw_walls(maze)

    # create the micromouse and solve the maze
    mouse = mm.Micromouse(start, target, maze)
    # Traverse the maze
    mouse.FloodFill()


if __name__ == "__main__":
    start = tuple([int(x) for x in input("Start: ").split(',')])
    target = tuple([int(x) for x in input("Target: ").split(',')])
    filepath = argv[1]
    draw('maze2.txt', start, target)
    mainloop()

