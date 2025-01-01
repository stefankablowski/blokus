from enum import Enum

class Color(Enum):
    RED = 1
    BLUE = 2
    YELLOW = 3
    GREEN = 4
    HIGHLIGHT = 5
    MAGENTA = 6
    WHITE = 7


def init_background_colors(curs):
    curs.start_color()
    
    # init background colors
    curs.init_pair(1, curs.COLOR_RED, curs.COLOR_RED)
    curs.init_pair(2, curs.COLOR_BLUE, curs.COLOR_BLUE)
    curs.init_pair(3, curs.COLOR_YELLOW, curs.COLOR_YELLOW)
    curs.init_pair(4, curs.COLOR_GREEN, curs.COLOR_GREEN)
    curs.init_pair(5, curs.COLOR_CYAN, curs.COLOR_CYAN)
    curs.init_pair(6, curs.COLOR_WHITE, curs.COLOR_WHITE)
    
    color_map = {
        Color.RED.value: curs.color_pair(1),
        Color.BLUE.value: curs.color_pair(2),
        Color.YELLOW.value: curs.color_pair(3),
        Color.GREEN.value: curs.color_pair(4),
        Color.HIGHLIGHT.value: curs.color_pair(5),
        Color.WHITE.value: curs.color_pair(6)
    }
    
    return color_map

def init_foreground_colors(curs):
    curs.start_color()
    curs.use_default_colors()
    
    # init foreground colors
    curs.init_pair(10, curs.COLOR_RED, curs.COLOR_BLACK)
    curs.init_pair(11, curs.COLOR_BLUE, curs.COLOR_BLACK)
    curs.init_pair(12, curs.COLOR_YELLOW, curs.COLOR_BLACK)
    curs.init_pair(13, curs.COLOR_GREEN, curs.COLOR_BLACK)
    curs.init_pair(14, curs.COLOR_MAGENTA, curs.COLOR_BLACK)
    curs.init_pair(15, curs.COLOR_WHITE, curs.COLOR_BLACK)
    curs.init_pair(16, curs.COLOR_CYAN, curs.COLOR_BLACK)
    
    color_map = {
        Color.RED.value: curs.color_pair(10),
        Color.BLUE.value: curs.color_pair(11),
        Color.YELLOW.value: curs.color_pair(12),
        Color.GREEN.value: curs.color_pair(13),
        Color.MAGENTA.value: curs.color_pair(14),
        Color.WHITE.value: curs.color_pair(15),
        Color.HIGHLIGHT.value: curs.color_pair(16),
    }
    
    return color_map

def init_combined_colors(curs):
    curs.start_color()
    curs.use_default_colors()
    
    # init foreground colors
    curs.init_pair(20, curs.COLOR_WHITE, curs.COLOR_RED)
    curs.init_pair(21, curs.COLOR_WHITE, curs.COLOR_BLUE)
    curs.init_pair(22, curs.COLOR_BLACK, curs.COLOR_YELLOW)
    curs.init_pair(23, curs.COLOR_BLACK, curs.COLOR_GREEN)
    curs.init_pair(24, curs.COLOR_WHITE, curs.COLOR_MAGENTA)
    curs.init_pair(25, curs.COLOR_WHITE, curs.COLOR_WHITE)
    curs.init_pair(26, curs.COLOR_WHITE, curs.COLOR_CYAN)
    
    color_map = {
        Color.RED.value: curs.color_pair(20),
        Color.BLUE.value: curs.color_pair(21),
        Color.YELLOW.value: curs.color_pair(22),
        Color.GREEN.value: curs.color_pair(23),
        Color.MAGENTA.value: curs.color_pair(24),
        Color.WHITE.value: curs.color_pair(25),
        Color.HIGHLIGHT.value: curs.color_pair(26),
    }
    
    return color_map