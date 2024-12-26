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
        self.reset_grid()

    def reset_grid(self):
        self.grid = [[None for _ in range(self.size)] for _ in range(self.size)]

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

def print_grid(self):
    color_map = {
        Color.RED.value: "\033[91mR\033[0m",
        Color.BLUE.value: "\033[94mB\033[0m",
        Color.YELLOW.value: "\033[93mY\033[0m",
        Color.GREEN.value: "\033[92mG\033[0m"
    }
    print()
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

def color_correct(self, color, start_pos, matrix):
    start_x, start_y = start_pos
    for i, row in enumerate(matrix):
        for j, cell in enumerate(row):
            if cell:
                x, y = start_x + i, start_y + j
                if not (0 <= x < self.size and 0 <= y < self.size):
                    return False
                # Check adjacent cells
                for dx, dy in [(-1, 0), (1, 0), (0, -1), (0, 1)]:
                    adj_x, adj_y = x + dx, y + dy
                    if 0 <= adj_x < self.size and 0 <= adj_y < self.size:
                        adj_value = self.grid[adj_x][adj_y]
                        if adj_value is not None and adj_value[0] == color.value:
                            return False
    return True

Grid.color_correct = color_correct

def connection_correct(self, color, start_pos, matrix):
    start_x, start_y = start_pos
    for i, row in enumerate(matrix):
        for j, cell in enumerate(row):
            if cell:
                x, y = start_x + i, start_y + j
                if not (0 <= x < self.size and 0 <= y < self.size):
                    return False
                # Check diagonal cells
                for dx, dy in [(-1, -1), (-1, 1), (1, -1), (1, 1)]:
                    diag_x, diag_y = x + dx, y + dy
                    if 0 <= diag_x < self.size and 0 <= diag_y < self.size:
                        diag_value = self.grid[diag_x][diag_y]
                        if diag_value is not None and diag_value[0] == color.value:
                            return True
    return False

Grid.connection_correct = connection_correct

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
