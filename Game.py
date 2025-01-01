from Grid import Grid, Color
from Player import Player
from Tile import Tile
from Color import Color

class Game:
    def __init__(self, curs):
        self.grid = Grid(curs)
        self.players = []

    def init_game(self):
        """
        Initializes the game by resetting the grid and setting up the players.

        This method performs the following actions:
        1. Resets the game grid.
        2. Initializes four players with the colors Red, Blue, Yellow, and Green.
        3. Each player draws their initial set of tiles from the available tiles.

        Returns:
            None
        """
        self.grid.reset_grid()
        self.players = [
            Player(Color.RED),
            Player(Color.BLUE),
            Player(Color.YELLOW),
            Player(Color.GREEN)
        ]
        for player in self.players:
            player.draw_tiles(Tile.all_tiles)
            
    def determine_winner(self):
        """
        Determines the winner of the game based on the player with the least remaining squares.

        Returns:
            Player: The player with the least remaining squares.
        """
        min = None
        min_player = None
        for player in self.players:
            remaining_squares = player.count_remaining_squares()
            if min is None or remaining_squares < min:
                min = remaining_squares
                min_player = player
        return min_player
    
    def is_move_possible(self, curr_player, grid, turn):
        if turn > 0:
            for handtile in curr_player.hand:
                for x_new in range(grid.size):
                    for y_new in range(grid.size):
                        if curr_player.play_tile(grid, (x_new, y_new), handtile, False):
                            return True
            return False
        else:
            return True

    def get_possible_move(self, curr_player, grid, turn):

        for handtile in curr_player.hand:
            for x_new in range(grid.size):
                for y_new in range(grid.size):
                    tried_position = curr_player.try_tile(grid, (x_new, y_new), handtile, turn, curr_player)
                    if tried_position is not None:
                        return ((x_new, y_new), handtile, *tried_position)
        return None




