from enum import Enum
import curses

class Color(Enum):
    RED = 1
    BLUE = 2
    YELLOW = 3
    GREEN = 4
    HIGHLIGHT = 5
    


def init_colors():
    curses.start_color()
    curses.init_pair(1, curses.COLOR_RED, curses.COLOR_RED)
    curses.init_pair(2, curses.COLOR_BLUE, curses.COLOR_BLUE)
    curses.init_pair(3, curses.COLOR_YELLOW, curses.COLOR_YELLOW)
    curses.init_pair(4, curses.COLOR_GREEN, curses.COLOR_GREEN)
    curses.init_pair(5, curses.COLOR_CYAN, curses.COLOR_CYAN)
    curses.init_pair(6, curses.COLOR_WHITE, curses.COLOR_WHITE)
    
    color_map = {
        Color.RED.value: curses.color_pair(1),
        Color.BLUE.value: curses.color_pair(2),
        Color.YELLOW.value: curses.color_pair(3),
        Color.GREEN.value: curses.color_pair(4),
        Color.HIGHLIGHT.value : curses.color_pair(5)  # Highlight
    }
    
    return color_map