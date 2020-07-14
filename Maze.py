class Maze:
    """
        A class for repersenting mazes
    """
    def __init__(self, height=10, width=10, walls=[], start=(0,0), end=None):
        """
            walls should be an array of tuples, with the first value being the x coord and the second value being the y coord of a cell (indexed at 0 with the top left corner being 0,0) that you cannot pass through
            start and end are tuples as well, with the same indexing as the walls
        """
        self.start = start
        self.specials = {} # for displaying, key as a tuple of a cell coord, and the value as the character that you would like to be displayed
        self.height = height
        self.width = width
        # if end is undefined, define it as the bottom left corner
        if(end):
            self.end = end
        else:
            self.end = (width - 1, height - 1)
        # create the grid that represents the maze
        self.grid = [[0 for _ in range(height)] for _ in range(width)]
        # add the walls, 0 being not a wall, 1 being a wall
        for row, col in walls:
            self.grid[col][row] = 1


    def __repr__(self):
        return_string = (self.width + 2) * "░░"
        return_string += "\n"
        for col in range(len(self.grid)):
            return_string += "░░"
            for row in range(len(self.grid[col])):
                cell = self.grid[col][row]
                if((row, col) == self.start):
                    return_string += "SS"
                elif((row, col) == self.end):
                    return_string += "EE"
                elif(cell == 1):
                    return_string += "██"
                elif((row, col) in self.specials):
                    return_string += self.specials[(row, col)] * 2
                elif(cell == 0):
                    return_string += "  "
                else:
                    return_string += str(cell)*2
            return_string += "░░"
            return_string += "\n"
        return_string += (self.width + 2) * "░░"

        return return_string

    
    
