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

def rotate_tile(matrix, rotations):
    rotations = rotations % 4
    for _ in range(rotations):
        matrix = [list(row) for row in zip(*matrix[::-1])]
    return matrix

Grid.rotate_tile = rotate_tile

def tile_fits(self, color, start_pos, matrix):
    start_x, start_y = start_pos
    for i, row in enumerate(matrix):
        for j, cell in enumerate(row):
            if cell:
                x, y = start_x + i, start_y + j
                if not (0 <= x < self.size and 0 <= y < self.size):
                    return False
                if self.grid[x][y] is not None:
                    return False
    return True

Grid.tile_fits = tile_fits

# Example usage
tile_matrix = [
    [True, False, False],
    [True, True, True],
    [False, False, True]
]

tile_matrix = rotate_tile(tile_matrix, 1)

global_grid.add_tile(Color.RED, (0, 0), Color.RED.value, tile_matrix)

# Example usage

# Adding 21 separate add_tile calls with unique matrices
# global_grid.add_tile(Color.RED, (0, 0), 1, [
#     [True]
# ])
# global_grid.add_tile(Color.RED, (0, 0), 2, [
#     [True, True] 
# ])
# global_grid.add_tile(Color.RED, (0, 0), 3, [
#     [True, True, True]
# ])
# global_grid.add_tile(Color.RED, (0, 0), 4, [
#     [True, True, True, True]
# ])
# global_grid.add_tile(Color.RED, (0, 0), 5, [
#     [True, True, True, True, True]
# ])
# global_grid.add_tile(Color.RED, (0, 0), 6, [
#     [True, True],
#     [True, True]
# ])
# global_grid.add_tile(Color.RED, (0, 0), 7, [
#     [True, True, False],
#     [False, True, True]
# ])
# global_grid.add_tile(Color.RED, (0, 0), 8, [
#     [True, True],
#     [True, False]
# ])
# global_grid.add_tile(Color.RED, (0, 0), 9, [
#     [True, False, False],
#     [True, True, True]
# ])
# global_grid.add_tile(Color.RED, (0, 0), 10, [
#     [False, False, True, True],
#     [True, True, True, False]
# ])
# global_grid.add_tile(Color.RED, (0, 0), 11, [
#     [True, True, True],
#     [False, True, False]
# ])
# global_grid.add_tile(Color.RED, (0, 0), 12, [
#     [True, True, True, True],
#     [False, True, False, False]
# ])
# global_grid.add_tile(Color.RED, (0, 0), 13, [
#     [False, True, False],
#     [True, True, True],
#     [False, False, True]
    
# ])
# global_grid.add_tile(Color.RED, (0, 0), 14, [
#     [True, True, True, True],
#     [False, False, False, True]
# ])
# global_grid.add_tile(Color.RED, (0, 0), 15, [
#     [True, True, True],
#     [False, True, False],
#     [False, True, False]
# ])
# global_grid.add_tile(Color.RED, (0, 0), 16, [
#     [True, True, True],
#     [True, False, False],
#     [True, False, False]
# ])
# global_grid.add_tile(Color.RED, (0, 0), 17, [
#     [False, True, False],
#     [True, True, True],
#     [False, True, False]
# ])
# global_grid.add_tile(Color.RED, (0, 0), 18, [
#     [True, True, True],
#     [False, True, True]
# ])
# global_grid.add_tile(Color.RED, (0, 0), 19, [
#     [True, False, False],
#     [True, True, True],
#     [False, False, True]
# ])
# global_grid.add_tile(Color.RED, (0, 0), 20, [
#     [False, True, False],
#     [True, True, True],
#     [True, False, False]
# ])
# global_grid.add_tile(Color.RED, (0, 0), 21, [
#     [True, True, True],
#     [True, False, True]
# ])

global_grid.print_grid()