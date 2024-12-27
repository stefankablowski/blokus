from Color import Color

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
            Color.RED.value: "\033[41m  \033[0m",
            Color.BLUE.value: "\033[44m  \033[0m",
            Color.YELLOW.value: "\033[43m  \033[0m",
            Color.GREEN.value: "\033[42m  \033[0m"
        }
        frame_color = "\033[47;1m  \033[0m"  # Light grey color for the frame
        print("\ny --> ")
        
        # Print top frame
        print(frame_color * (self.size + 2))
        
        for row in self.grid:
            # Print left frame
            print(frame_color, end="")
            for cell in row:
                if cell is None:
                    print("  ", end="")
                else:
                    print(color_map.get(cell[0], "  "), end="")
            # Print right frame
            print(frame_color)
        
        # Print bottom frame
        print(frame_color * (self.size + 2))

    def print_grid_overlay(self, color, start_pos, matrix):
        overlay_grid = [row[:] for row in self.grid]
        start_x, start_y = start_pos
        for i, row in enumerate(matrix):
            for j, cell in enumerate(row):
                if cell:
                    overlay_grid[start_x + i][start_y + j] = (color, None)

        color_map = {
            Color.RED.value: "\033[41m  \033[0m",
            Color.BLUE.value: "\033[44m  \033[0m",
            Color.YELLOW.value: "\033[43m  \033[0m",
            Color.GREEN.value: "\033[42m  \033[0m"
        }
        frame_color = "\033[47;1m  \033[0m"  # Light grey color for the frame
        print("\ny --> ")
        
        # Print top frame
        print(frame_color * (self.size + 2))
        
        for row in overlay_grid:
            # Print left frame
            print(frame_color, end="")
            for cell in row:
                if cell is None:
                    print("  ", end="")
                else:
                    print(color_map.get(cell[0], "  "), end="")
            # Print right frame
            print(frame_color)
        
        # Print bottom frame
        print(frame_color * (self.size + 2))

    def add_tile(self, color, start_pos, tile_number, matrix):
        start_x, start_y = start_pos
        for i, row in enumerate(matrix):
            for j, cell in enumerate(row):
                if cell:
                    self.set_value(start_x + i, start_y + j, (color, tile_number))

    # Add the add_tile method to the Grid class


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
                            if adj_value is not None and adj_value[0] == color:
                                return False
        return True

    # Returns true if for any cell of the pattern there is a diagonal cell in the grid of the same color
    def connection_possibly_correct(self, color, start_pos, matrix):
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
                            if diag_value is not None and diag_value[0] == color:
                                return True
        return False
    
    def matches_start_position(self, start_pos, matrix):
        start_x, start_y = start_pos
        for i, row in enumerate(matrix):
            for j, cell in enumerate(row):
                if cell and (start_x + i == start_x) and (start_y + j == start_y):
                    return True
        return False
