from Grid import Grid, Color
from Player import Player
from Tile import Tile
from Color import Color

class Game:
    def __init__(self):
        self.grid = Grid()
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
            


