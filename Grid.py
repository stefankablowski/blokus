from Color import Color, init_background_colors
import curses

class Grid:
    def __init__(self, curs, size=20):
        self.size = size
        self.reset_grid()
        self.color_map = init_background_colors(curs)

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
            Color.GREEN.value: "\033[42m  \033[0m",
            'ORANGE': "\033[48;5;208m  \033[0m"  # Orange color
        }
        frame_color = "\033[47;1m  \033[0m"  # Light grey color for the frame
        print("\ny --> ")
        
        # Print top frame
        print(frame_color * (self.size + 2))
        
        for i, row in enumerate(overlay_grid):
            # Print left frame
            print(frame_color, end="")
            for j, cell in enumerate(row):
                if (i, j) == start_pos:
                    print(color_map['ORANGE'], end="")
                elif cell is None:
                    print("  ", end="")
                else:
                    print(color_map.get(cell[0], "  "), end="")
            # Print right frame
            print(frame_color)
        
        # Print bottom frame
        print(frame_color * (self.size + 2))
        
    def print_grid_overlay_stdscr(self, stdscr, curs, start_pos=None, matrix=None, color=Color.HIGHLIGHT.value):
        
        color_map = init_background_colors(curs)
        
        overlay_grid = [row[:] for row in self.grid]
        if matrix is not None and start_pos is not None:
            start_x, start_y = start_pos
            for i, row in enumerate(matrix):
                for j, cell in enumerate(row):
                    if cell:
                        overlay_grid[start_x + i][start_y + j] = (color, None)


        frame_color = color_map.get(Color.WHITE.value)

        stdscr.addstr(0, 0, "B L O K U S")

        # Print top frame
        for i in range(self.size + 2):
            stdscr.addstr(1, i * 2, "  ", frame_color)

        for i, row in enumerate(overlay_grid):
            # Print left frame
            stdscr.addstr(i + 2, 0, "  ", frame_color)
            for j, cell in enumerate(row):
                if cell is None:
                    stdscr.addstr(i + 2, (j + 1) * 2, "  ")
                else:
                    stdscr.addstr(i + 2, (j + 1) * 2, "  ", color_map.get(cell[0], curses.A_NORMAL))
            # Print right frame
            stdscr.addstr(i + 2, (self.size + 1) * 2, "  ", frame_color)

        # Print bottom frame
        for i in range(self.size + 2):
            stdscr.addstr(self.size + 2, i * 2, "  ", frame_color)

        stdscr.refresh()
        
    def print_player_bar(self, stdscr, color_map,  all_players, active_players, player_index):

        stdscr.addstr(self.size + 3, 0, 10*6*" ")
        stdscr.refresh()
        stdscr.addstr(self.size + 3, 0, "Players: ")
        for idx, player in enumerate(all_players):
            player_symbol = "X" if player not in active_players else "O"
            player_score = player.count_remaining_squares()
            output = f"{player_symbol} {player_score}"
            stdscr.addstr(self.size + 3, 10 + idx * 6, output, color_map[player.color])
        stdscr.refresh()

    def add_tile(self, color, start_pos, tile_number, matrix):
        start_x, start_y = start_pos
        for i, row in enumerate(matrix):
            for j, cell in enumerate(row):
                if cell:
                    self.set_value(start_x + i, start_y + j, (color, tile_number))

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
    
    def matches_start_position(self, start_pos, current_pos, matrix):
        start_x, start_y = start_pos
        current_x, current_y = current_pos
        for i, row in enumerate(matrix):
            for j, cell in enumerate(row):
                if cell and (current_x + i == start_x) and (current_y + j == start_y):
                    return True
        return False
    
    def print_notification(self, stdscr, text):
        stdscr.addstr(self.size + 4, 0, f" "*self.size)
        stdscr.addstr(self.size + 4, 0, f"{text}")
  
    def determine_start_position(self, colornumber):
        if colornumber == 1:
            position = (0, 0)  # Top left corner
        elif colornumber == 2:
            position = (0, self.size - 1)  # Top right corner
        elif colornumber == 3:
            position = (self.size - 1, 0)  # Bottom left corner
        elif colornumber == 4:
            position = (self.size - 1, self.size - 1)  # Bottom right corner
        else:
            raise ValueError("Invalid colornumber. Must be 1, 2, 3, or 4.")
        return position
