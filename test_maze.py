from Maze import Maze
from a_star import a_star

small_maze = [(1,0), (1, 1), (0, 4), (1, 4), (2, 3), (3, 1), (3, 2), (3, 3), (3, 4)]
large_maze = [(0, 3), (1, 0), (1, 1), (1, 3), (1, 4), (1, 5), (1, 7), (1, 8), (1, 9), (3, 0), (3, 1), (3, 2), (3, 3), (3, 5), (3, 7), (3, 8), (3, 9), (4, 5), (5, 1), (5, 3), (5, 5), (5, 6), (5, 7), (5, 9), (5, 10), (6, 1), (6, 3), (7, 1), (7, 3), (7, 5), (7, 6), (7, 7), (7, 9), (8, 0), (8, 1), (8, 5), (8, 9), (9, 1), (9, 3), (9, 4), (9, 5), (9, 7), (9, 8), (9, 9), (10, 1), (10, 7)]
small_maze_no_solution = [(4, 3), (3, 4)]

def test_make_maze():
    my_maze = Maze(5, 5, small_maze)
    assert(my_maze)

def test_manhattan():
    my_maze = Maze(11, 11, large_maze)
    assert(my_maze)
    path = a_star(my_maze, h_type=2)
    assert(len(path) == 21)
    assert(path[0] == (0, 0))
    assert(path[-1] == (10, 10))

def test_diagonal():
    my_maze = Maze(11, 11, large_maze)
    assert(my_maze)
    path = a_star(my_maze, h_type=1)
    assert(len(path) == 21)
    assert(path[0] == (0, 0))
    assert(path[-1] == (10, 10))

def test_euclidean():
    my_maze = Maze(11, 11, large_maze)
    assert(my_maze)
    path = a_star(my_maze, h_type=0)
    assert(len(path) == 21)
    assert(path[0] == (0, 0))
    assert(path[-1] == (10, 10))

def test_no_solution():
    my_maze = Maze(5, 5, small_maze_no_solution)
    assert(my_maze)
    try:
        a_star(my_maze)
    except(Exception):
        pass


    