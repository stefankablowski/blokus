import unittest
from Game import Game
import time


class TestGame(unittest.TestCase):
    def test_single_player_sequence(self):
        game = Game()
        game.init_game()
        self.assertEquals(game.grid.size, 20)
        self.assertEqual(len(game.players), 4)
        
        firstPlayer = game.players[0]
        firstPlayer.play_sequence(game.grid)
        
    def test_game_init(self):
        game = Game()
        game.init_game()
        grid = game.grid
        self.assertEquals(game.grid.size, 20)
        self.assertEqual(len(game.players), 4)
        
        for player in game.players:
            player.play_start_tile(game.grid, player.hand.pop(0), player.color)

        game.grid.print_grid()
        active_players = game.players.copy()
        curr_player_i = 0

        while len(active_players) > 1:
            
            player = active_players[curr_player_i]
            # get handtile
            handtile = player.hand.pop(0)
            placed = False
            for x in range(grid.size):
                for y in range(grid.size):
                    if player.play_tile(grid, (x,y), handtile):
                        placed = True
                        break
                if placed:
                    break
            if not placed:
                active_players.remove(player)
                print("Player " + player.name + " has no more moves")
            curr_player_i = (curr_player_i + 1) % len(active_players)
            grid.print_grid()
            time.sleep(0.5)
        
        # all players must make their initial move
        # while loop
        #   a player makes a move using a tile from his hand
        #   the tile is removed from his hand
        
