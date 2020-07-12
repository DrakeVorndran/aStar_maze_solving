from Maze import Maze

test_tuples = [(1,0), (1, 1), (0, 4), (1, 4), (2, 3), (3, 1), (3, 2), (3, 3), (3, 4)]


def test_make_maze():
    my_maze = Maze(5, 5, test_tuples)
    assert(my_maze)
    