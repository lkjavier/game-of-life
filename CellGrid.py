"""
This is an implementation of Conway's game of life in Python.
Without any arguments the constructor will create a 20x20 grid with a blinker somewhat in the middle

>>> x = CellGrid()
>>> x.state[10][11]
1

"""
import copy
import json
import time
import random

class CellGrid:
    """
    Class for creating a grid of cells that can be either dead or alive.
    Default size is 20x20, living cells are represented by 1, non-living cells by 0
    """
    def __init__(self, size = 20, state = [[10,10], [10,11], [10,12]]):
        self.state = [[0 for i in range(0, size)] for i in range(0, size)]
        self.size = size
        for cell in state:
            self.set_cell(cell[0], cell[1])   
        self.new_state = copy.deepcopy(self.state)
        
    def randomize(self):
        n = 0
        while n < self.size*self.size / 4 :
            self.set_cell(random.randint(0, self.size -1), random.randint(0,self.size -1))
            n += 1
        
    def print_n_steps(self, n):
        count = 0
        while count < n:
            self.advance()
            clear_output()
            for i in self.state:
                display(i)
            time.sleep(1)
            count += 1
    
    def print_state(self):
        for i in self.state:
            print(i)
        
    def get_json_state(self):
        return json.dumps(self.state)
    
    def advance(self):
        for indexX, row in enumerate(self.state):
            for indexY, cell in enumerate(row):
                neighbour_count = self.count_neighbours(indexX, indexY)
                if cell == 0:
                    if neighbour_count == 3:
                        self.new_state[indexX][indexY] = 1
                if cell == 1:
                    if neighbour_count < 2 or neighbour_count > 3:
                        self.new_state[indexX][indexY] = 0
        self.state = copy.deepcopy(self.new_state)
                    
        
    def set_cell(self, x, y, value = 1):
        if self.out_of_bounds(x) or self.out_of_bounds(y):
            raise ValueError('CellGrid.set_cell: One or more coordinates out of bounds.\nX:{} \nY:{} \nSize:{}'.format(x, y, self.size))
        self.state[x][y] = value
        
        
    def count_neighbours(self, x, y):
        count = 0
        if self.out_of_bounds(x) or self.out_of_bounds(y):
             raise ValueError('CellGrid.set_cell: One or more coordinates out of bounds.\nX:{} \nY:{} \nSize:{}'.format(x, y, self.size)) 
        
        for i in range(x-1, x+2):
            if not self.out_of_bounds(i):
                for j in range(y-1, y+2):
                    if not self.out_of_bounds(j) and not (i == x and j == y):
                        count += self.state[i][j]                 
        return count
    
    def out_of_bounds(self, coordinate):
        if coordinate < 0 or coordinate >= self.size:
            return True
        return False

if __name__ == "__main__":
    import doctest
    doctest.testmod()