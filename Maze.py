class Maze:
    def __init__(self, height=10, width=10, walls=[], start=(0,0), end=None):
        self.start = start
        self.specials = {}
        self.height = height
        self.width = width
        if(end):
            self.end = end
        else:
            self.end = (width - 1, height - 1)
        self.grid = [[0 for _ in range(height)] for _ in range(width)]
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

    
    
