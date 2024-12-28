import unittest
import curses
from SinglePlayer import print_end_screen
from Grid import Grid
from Color import Color
from Player import Player


stdscr = curses.initscr()
grid = Grid()
player = Player(Color.GREEN)

def test_print_end_screen():
    print_end_screen(stdscr, player, grid)
    while True:
        key = stdscr.getch()
        if key == ord('q'):
            break
        
test_print_end_screen()