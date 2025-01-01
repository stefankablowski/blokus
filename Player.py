from Tile import Tile


class Player:
    def __init__(self, colorAndName):
        self.name = colorAndName.name
        self.color = colorAndName.value
        self.hand = []

    def draw_tiles(self, all_tiles):
        self.hand = [(index, tile) for index, tile in enumerate(all_tiles)]

    def play_tile(self, grid, position, handtile, actually_play=True):
        index, matrix = handtile
        for mirrored in [True, False]:
            rotated_matrix = Tile.mirror_tile(matrix, vertical=mirrored)
            for rotations in range(4):
                rotated_matrix = Tile.rotate_tile(matrix, rotations)
                if grid.tile_fits(self.color, position, rotated_matrix):
                    if grid.color_correct(self.color, position, rotated_matrix) and grid.connection_possibly_correct(self.color, position, rotated_matrix):
                        if actually_play:
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
    
    def count_remaining_squares(self):
        count = 0
        for _, tile in self.hand:
            count += sum(row.count(True) for row in tile)
        return count
    
    def try_tile(self, grid, position, handtile, turn, player):
        colornumber = player.color
        
        index, matrix = handtile
        for mirrored in [True, False]:
            rotated_matrix = Tile.mirror_tile(matrix, vertical=mirrored)
            for rotations in range(4):
                rotated_matrix = Tile.rotate_tile(matrix, rotations)
                               
                if grid.tile_fits(self.color, position, rotated_matrix):
                    if (grid.color_correct(self.color, position, rotated_matrix) and grid.connection_possibly_correct(self.color, position, rotated_matrix)):
                        return (mirrored, rotations)
                    
                    start_position = grid.determine_start_position(colornumber)
                    matches_start = grid.matches_start_position(start_position, position, rotated_matrix)
                    if (turn < 4) and matches_start:
                        return (mirrored, rotations)
        return None
    
    def do_move(self, grid, handtile, position, mirrored, rotations):
        
        index, matrix = handtile
        rotated_matrix = Tile.mirror_tile(matrix, vertical=mirrored)
        rotated_matrix = Tile.rotate_tile(matrix, rotations)
        grid.add_tile(self.color, position, index, rotated_matrix)
        
        # remove tile from hand
        self.hand.remove(handtile)