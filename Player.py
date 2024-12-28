from Tile import Tile


class Player:
    def __init__(self, colorAndName):
        self.name = colorAndName.name
        self.color = colorAndName.value
        self.hand = []

    def draw_tiles(self, all_tiles):
        self.hand = [(index, tile) for index, tile in enumerate(all_tiles)]

    def play_tile(self, grid, position, handtile):
        index, matrix = handtile
        for mirrored in [True, False]:
            rotated_matrix = Tile.mirror_tile(matrix, vertical=mirrored)
            for rotations in range(4):
                rotated_matrix = Tile.rotate_tile(matrix, rotations)
                if grid.tile_fits(self.color, position, rotated_matrix):
                    if grid.color_correct(self.color, position, rotated_matrix) and grid.connection_possibly_correct(self.color, position, rotated_matrix):
                        grid.add_tile(self.color, position, index, rotated_matrix)
                        return True
        return False
    
    def play_sequence(self, grid):
        
        self.play_start_tile(grid, self.hand[0], self.color)
        for handtile in self.hand:
            placed = False
            for x in range(grid.size):
                for y in range(grid.size):
                    if self.play_tile(grid, (x, y), handtile):
                        placed = True
                        break
                if placed:
                    break
        grid.print_grid()
        
    def play_start_tile(self, grid, handtile, colornumber):
        
        if colornumber == 1:
            position = (0, 0)  # Top left corner
        elif colornumber == 2:
            position = (0, grid.size - 1)  # Top right corner
        elif colornumber == 3:
            position = (grid.size - 1, 0)  # Bottom left corner
        elif colornumber == 4:
            position = (grid.size - 1, grid.size - 1)  # Bottom right corner
        else:
            raise ValueError("Invalid colornumber. Must be 1, 2, 3, or 4.")
        
        index, matrix = handtile
        for mirrored in [True, False]:
            rotated_matrix = Tile.mirror_tile(matrix, vertical=mirrored)
            for rotations in range(4):
                rotated_matrix = Tile.rotate_tile(matrix, rotations)
                if grid.tile_fits(self.color, position, rotated_matrix) and grid.matches_start_position(position, position, rotated_matrix):
                    grid.add_tile(self.color, position, index, rotated_matrix)
                    return True
        return False