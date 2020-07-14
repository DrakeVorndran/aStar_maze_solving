from Maze import Maze
from dataclasses import dataclass
from math import sqrt


# Data class used to represent single cells
@dataclass
class DataClassCell:
    cell: tuple
    parent: object
    g: int
    h: int
    f: int

# https://www.geeksforgeeks.org/a-search-algorithm/ explanation and walkthrough
def a_star(maze, v=False, h_type=0):
    """
        takes a maze object, and returns a set of tuples describing a shortest path from the mazes start and end
        v is a boolean repersenting verbose, this will print out the maze at every step, showing what cells have been visited, as well as what cells have been seen
    """


    def calc_h(cell):
        """ 
            calculates the heuristic distance from the given cell to the end of the maze
            The type of calculation depends on the h_type, which changes how the algorithm reacts
        """
        if(h_type == 0):
            # Euclidean Distance
            return sqrt(((cell[0] - maze.end[0])**2) + ((cell[1] - maze.end[1])**2))
        elif(h_type == 1):
            # Diagonal Distance
            return max(abs(cell[0] - maze.end[0]), abs(cell[1] - maze.end[1]))
        else:
            # Manhattan Distance
            return abs(cell[0] - maze.end[0]) + abs(cell[1] - maze.end[1])

    def make_path(data_cell):
        """ returns a list of the ordered path """
        l = [data_cell.cell]
        current_cell = data_cell.parent
        while current_cell != None:
            l.append(current_cell.cell)
            current_cell = current_cell.parent
        l.reverse()
        return l

    open_list = {} # all of the cells that we have seen, but havent visited
    closed_list = {} # all the cells we have visited
    # add the starting cell to the open list, starting our loop
    open_list[maze.start] = (DataClassCell(maze.start, None, 0, calc_h(maze.start), calc_h(maze.start)))
    # while there are still cells we have yet to visit
    while len(open_list) > 0:
        if v:
            print(maze)
            print(" ")
        # find the lowest value of "f" which is the closest cell we have to the end
        lowest = None
        for data_cell in open_list.values():
            if lowest == None:
                lowest = data_cell
            if lowest.f > data_cell.f:
                lowest = data_cell
        best_cell = lowest.cell
        current_cell = open_list.pop(best_cell)
        closed_list[current_cell.cell] = current_cell 
        if(v):
            maze.specials[current_cell.cell] = "c"
        # for looping to dry up code when I am checking the directions
        l1 = [0, 1, 0, -1]
        for change in range(len(l1)):
            # getting the row and col for the current successor -> (row, col)
            successor = (current_cell.cell[0] + l1[change], (current_cell.cell[1] + l1[(change + 1) % len(l1)]))
            # if the cell we are checking is within the maze
            if not (successor[0] < 0 or successor[0] > maze.width - 1 or successor[1] < 0 or successor[1] > maze.height - 1):
                # if the cell we are checking has not yet been visited
                if(successor not in closed_list):
                    # calculate the distance from the start "g" and the heuristic distance from the end "h"
                    new_g = current_cell.g + 1
                    new_h = calc_h(successor)
                    new_f = new_g + new_h
                    # create a cell object that repersents the successor we are currently checking
                    new_cell = DataClassCell(successor, current_cell,  new_g, new_h, new_f)
                    # if we have never seen the cell before
                    if(successor not in open_list):
                        # if the cell we are checking is an empty space, not a wall
                        if maze.grid[successor[1]][successor[0]] == 0:
                            # if the cell we are checking is the end of the maze
                            if(maze.end == successor):
                                # return the path from the begining of the maze, to the successor (end of the maze)
                                return make_path(new_cell)
                            # add the successor to the open_list, to be checked later
                            open_list[successor] = new_cell
                            if(v):
                                maze.specials[successor] = "o"
                    # we have seen the cell before, but have not checked it yet
                    else:
                        # if the path we have taken is shorter than the previous path to the cell
                        if open_list[successor].parent.g > current_cell.g:
                            # changes the parent of the successor, and updates the distance
                            open_list[successor] = new_cell
                            if(v):
                                maze.specials[successor] = "o"
    raise Exception("no path found")
                


        
