from Maze import Maze
from a_star import a_star

if __name__ == "__main__":
    test_tuples = [(1,0), (1, 1), (0, 4), (1, 4), (2, 3), (3, 1), (3, 2), (3, 3), (3, 4)]
    my_maze = Maze(5, 5, [(1, 0), (2, 1), (3, 3), (1, 2)], start=(0, 0))

    print(my_maze)
    print(a_star(my_maze, True))