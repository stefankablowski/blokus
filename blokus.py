from enum import Enum

# Example usage
class Color(Enum):
    RED = 1
    BLUE = 2
    YELLOW = 3
    GREEN = 4

class Grid:
    def __init__(self, size=20):
        self.size = size
        self.grid = [[None for _ in range(size)] for _ in range(size)]

    def set_value(self, x, y, value):
        if 0 <= x < self.size and 0 <= y < self.size:
            self.grid[x][y] = value
        else:
            raise IndexError("Grid coordinates out of range")

    def get_value(self, x, y):
        if 0 <= x < self.size and 0 <= y < self.size:
            return self.grid[x][y]
        else:
            raise IndexError("Grid coordinates out of range")

# Example usage
global_grid = Grid()

# print(grid.get_value(5, 5))  # Output: (1, 2)

def print_grid(self):
    color_map = {
        Color.RED.value: "\033[91mR\033[0m",
        Color.BLUE.value: "\033[94mB\033[0m",
        Color.YELLOW.value: "\033[93mY\033[0m",
        Color.GREEN.value: "\033[92mG\033[0m"
    }
    for row in self.grid:
        for cell in row:
            if cell is None:
                print(".", end=" ")
            else:
                print(color_map.get(cell[0], "."), end=" ")
        print()

# Add the print_grid method to the Grid class
Grid.print_grid = print_grid

def add_tile(self, color, start_pos, tile_number, matrix):
    start_x, start_y = start_pos
    for i, row in enumerate(matrix):
        for j, cell in enumerate(row):
            if cell:
                self.set_value(start_x + i, start_y + j, (color.value, tile_number))

# Add the add_tile method to the Grid class
Grid.add_tile = add_tile

# Example usage
tile_matrix = [
    [True, False, False],
    [True, True, True],
    [False, False, True]
]

global_grid.add_tile(Color.RED, (0, 0), Color.RED.value, tile_matrix)

# Example usage
global_grid.set_value(0, 0, (Color.RED.value, 2))
global_grid.set_value(6, 6, (Color.BLUE.value, 2))
global_grid.set_value(7, 7, (Color.YELLOW.value, 2))
global_grid.set_value(8, 8, (Color.GREEN.value, 2))
global_grid.print_grid()