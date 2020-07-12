from Maze import Maze
from dataclasses import dataclass
from math import sqrt

@dataclass
class DataClassCell:
    cell: tuple
    parent: object
    g: int
    h: int
    f: int

# https://www.geeksforgeeks.org/a-search-algorithm/ explanation and walkthrough
def a_star(maze, v=False):
    
    def calc_h(cell):
        return ((cell[0] - maze.end[0])**2) + ((cell[1] - maze.end[1])**2)

    def make_path(data_cell):
        """ returns a list of the ordered path """
        l = [data_cell.cell]
        current_cell = data_cell.parent
        while current_cell != None:
            l.append(current_cell.cell)
            current_cell = current_cell.parent
        l.reverse()
        return l

    open_list = {}
    closed_list = {}
    open_list[maze.start] = (DataClassCell(maze.start, None, 0, calc_h(maze.start), calc_h(maze.start)))
    while len(open_list) > 0:
        if v:
            print(maze)
            print(" ")
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
            # print(successor)
            if not (successor[0] < 0 or successor[0] > maze.width - 1 or successor[1] < 0 or successor[1] > maze.height - 1):
                if(successor not in closed_list):
                    # print("not in closed list")
                    new_g = current_cell.g + 1
                    new_h = calc_h(successor)
                    new_f = new_g + new_h
                    new_cell = DataClassCell(successor, current_cell,  new_g, new_h, new_f)
                    if(successor not in open_list):
                        # print("not in open list")
                        if maze.grid[successor[1]][successor[0]] == 0:
                            if(maze.end == successor):
                                return make_path(new_cell)
                            open_list[successor] = new_cell
                            if(v):
                                maze.specials[successor] = "o"
                                # maze.specials[successor] = str(float(new_cell.f))
                    else:
                        if open_list[successor].parent.g > current_cell.g:
                            # changes the parent of the successor
                            open_list[successor] = new_cell
                            if(v):
                                maze.specials[successor] = "o"
                                # maze.specials[successor] = str(float(new_cell.f))
    return "no path found"
                


        
