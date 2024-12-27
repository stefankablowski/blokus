import unittest
from Grid import Grid, Color

class TestGrid(unittest.TestCase):
    def setUp(self):
        self.global_grid = Grid()

    # def test_set_and_get_value(self):
    #     self.grid.set_value(0, 0, (Color.RED.value, 1))
    #     self.assertEqual(self.grid.get_value(0, 0), (Color.RED.value, 1))

    # def test_set_value_out_of_range(self):
    #     with self.assertRaises(IndexError):
    #         self.grid.set_value(21, 21, (Color.RED.value, 1))

    # def test_get_value_out_of_range(self):
    #     with self.assertRaises(IndexError):
    #         self.grid.get_value(21, 21)

    # def test_add_tile(self):
    #     tile_matrix = [
    #         [True, False],
    #         [True, True]
    #     ]
    #     self.grid.add_tile(Color.BLUE, (0, 0), 1, tile_matrix)
    #     self.assertEqual(self.grid.get_value(0, 0), (Color.BLUE.value, 1))
    #     self.assertEqual(self.grid.get_value(1, 0), (Color.BLUE.value, 1))
    #     self.assertEqual(self.grid.get_value(1, 1), (Color.BLUE.value, 1))
        self.global_grid.reset_grid()

    def test_tile_fits(self):
        tile_matrix = [
            [True, True],
            [True, False]
        ]
        self.assertTrue(self.global_grid.tile_fits(Color.GREEN.value, (0, 0), tile_matrix))
        # Adding a tile to the grid at position (0, 0) with color GREEN and tile number 1
        self.global_grid.add_tile(Color.GREEN.value, (0, 0), 1, tile_matrix)
        self.global_grid.print_grid()
        self.assertFalse(self.global_grid.tile_fits(Color.GREEN.value, (0, 0), tile_matrix))
        self.assertFalse(self.global_grid.tile_fits(Color.GREEN.value, (1, 0), tile_matrix))
        self.assertFalse(self.global_grid.tile_fits(Color.GREEN.value, (0, 1), tile_matrix))
        self.assertTrue(self.global_grid.tile_fits(Color.GREEN.value, (1, 1), tile_matrix))
        self.global_grid.add_tile(Color.GREEN.value, (1, 1), 1, tile_matrix)
        self.global_grid.print_grid()
        self.global_grid.reset_grid()

    def test_color_correct(self):
        tile_matrix = [
            [True, False],
            [True, True]
        ]
        self.assertTrue(self.global_grid.color_correct(Color.YELLOW, (0, 0), tile_matrix))
        self.global_grid.add_tile(Color.YELLOW, (0, 0), 1, tile_matrix)
        self.global_grid.print_grid()
        
        self.assertFalse(self.global_grid.color_correct(Color.YELLOW, (1, 1), tile_matrix))
        #self.global_grid.add_tile(Color.YELLOW, (3, 0), 1, tile_matrix)
        self.global_grid.print_grid()
        
        self.assertTrue(self.global_grid.color_correct(Color.YELLOW, (3, 0), tile_matrix))
        self.global_grid.reset_grid()

    def test_connection_possibly_correct(self):
        tile_matrix = [
            [True, False],
            [True, True]
        ]
        self.assertFalse(self.global_grid.connection_possibly_correct(Color.RED, (0, 0), tile_matrix))
        self.global_grid.add_tile(Color.RED, (0, 0), 1, tile_matrix)
        self.assertTrue(self.global_grid.connection_possibly_correct(Color.RED, (1, 2), tile_matrix))
        self.global_grid.add_tile(Color.RED, (1, 2), 1, tile_matrix)
        self.global_grid.print_grid()
        
        # self.assertTrue(self.global_grid.connection_possibly_correct(Color.RED, (2, 2), tile_matrix))
        # self.global_grid.add_tile(Color.RED, (2, 2), 1, tile_matrix)
        # self.global_grid.print_grid()
        # self.global_grid.reset_grid()
        
        
    def test_run_game(self):
        self.global_grid.reset_grid()
        # Initialize the game
        # self.grid.initialize_game()
        
        # Simulate a series of moves
        moves = [
            (Color.RED, (0, 0), 1, [
                [True, False],
                [True, True]
            ]),
            (Color.BLUE, (2, 2), 2, [
                [True, True],
                [False, True]
            ]),
            (Color.GREEN.value, (4, 4), 3, [
                [True, True, True],
                [False, True, False]
            ]),
            (Color.YELLOW, (6, 6), 4, [
                [True, True, True, True]
            ])
        ]
        
        for color, position, tile_number, tile_matrix in moves:
            self.assertTrue(self.global_grid.tile_fits(color, position, tile_matrix))
            self.global_grid.add_tile(color, position, tile_number, tile_matrix)
            # self.grid.print_grid()
            
    def test_print_grid_overlay(self):
        
        tile_matrix = [
            [True, True],
            [True, False]
        ]

        # Adding a tile to the grid at position (0, 0) with color GREEN and tile number 1
        self.global_grid.add_tile(Color.GREEN.value, (0, 0), 1, tile_matrix)
        # self.global_grid.print_grid()
        self.global_grid.print_grid_overlay(Color.GREEN.value, (2, 2), tile_matrix)
            

