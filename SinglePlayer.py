import curses

from Color import Color
from Game import Game  
from Tile import Tile

def main(stdscr):
    
    print_welcome_message(stdscr)

    stdscr.clear()
    
    chosen_color = print_choose_color(stdscr)

    # Initial position of the dot
    x = 0
    y = 0
    
    tile_index = 0
    
    game = Game()
    game.init_game()
    grid = game.grid
    
    # determine the player of the chosen color
    # get player of the game players with the same color as the chosen color
    player = [player for player in game.players if player.color == chosen_color][0]
    
    i, tile_matrix = player.hand[tile_index]

    # Hide the cursor
    curses.curs_set(0)
        
    while True:
        # Clear the screen
        stdscr.clear()

        # Draw the dot at the current position
        grid.print_grid_overlay_stdscr(stdscr, chosen_color, (x, y), tile_matrix)

        # Refresh the screen
        stdscr.refresh()

        # Get user input
        key = stdscr.getch()

        # Move the dot based on the key input
        if key == curses.KEY_LEFT:
            y = max(0, y - 1)
        elif key == curses.KEY_RIGHT:
            y = min(curses.COLS - 1, y + 1)
        elif key == curses.KEY_UP:
            x = max(0, x - 1)
        elif key == curses.KEY_DOWN:
            x = min(curses.LINES - 1, x + 1)
        elif key == ord(' ') or key == ord('r'):
            tile_matrix = Tile.rotate_tile(tile_matrix, 1)
        elif key == curses.KEY_ENTER or key == 10:
            grid.add_tile(chosen_color, (x, y), tile_index, tile_matrix)
        # if key is x then decrement tile index but not below 0
        elif key == ord('y'):
            tile_index = max(0, tile_index - 1)
            i, tile_matrix = player.hand[tile_index]
        # if key is y then increment tile index but not above the length of the hand
        elif key == ord('x'):
            tile_index = min(len(player.hand) - 1, tile_index + 1)
            i, tile_matrix = player.hand[tile_index]
        # if key is m then mirror the tile
        elif key == ord('m'):
            tile_matrix = Tile.mirror_tile(tile_matrix, vertical=True)
            
        elif key == ord('q'):
            break
        
        
def print_welcome_message(stdscr):
    
    # Initialize colors
    curses.start_color()
    curses.init_pair(1, curses.COLOR_WHITE, curses.COLOR_BLACK)
    curses.init_pair(2, curses.COLOR_CYAN, curses.COLOR_BLACK)
    curses.init_pair(3, curses.COLOR_MAGENTA, curses.COLOR_BLACK)
    curses.init_pair(4, curses.COLOR_YELLOW, curses.COLOR_BLACK)
    curses.init_pair(5, curses.COLOR_GREEN, curses.COLOR_BLACK)
    curses.init_pair(6, curses.COLOR_RED, curses.COLOR_BLACK)

    stdscr.addstr(0, 0, "Welcome to the game!", curses.color_pair(1))
    stdscr.addstr(1, 0, "Use the arrow keys to move the tile", curses.color_pair(2))
    stdscr.addstr(2, 0, "Press 'q' to quit", curses.color_pair(3))
    stdscr.addstr(3, 0, "Press 'space' to rotate the tile", curses.color_pair(4))
    stdscr.addstr(4, 0, "Press 'Enter' to place the tile", curses.color_pair(5))
    stdscr.addstr(5, 0, "Press 'y' to select the previous tile", curses.color_pair(6))
    stdscr.addstr(6, 0, "Press 'x' to select the next tile", curses.color_pair(1))
    stdscr.addstr(7, 0, "Press 'm' to mirror the tile", curses.color_pair(2))
    stdscr.addstr(8, 0, "Press 'space' to start", curses.color_pair(3))
       
    stdscr.refresh()
    
    while True:
        key = stdscr.getch()
        if key == ord(' '):
            break
    
def print_choose_color(stdscr):
    
    color = Color.RED.value
    
    stdscr.addstr(0, 0, "Choose a color:")
    # Initialize colors
    curses.start_color()
    curses.init_pair(2, curses.COLOR_CYAN, curses.COLOR_BLACK)
    curses.init_pair(4, curses.COLOR_YELLOW, curses.COLOR_BLACK)
    curses.init_pair(5, curses.COLOR_GREEN, curses.COLOR_BLACK)
    curses.init_pair(6, curses.COLOR_RED, curses.COLOR_BLACK)

    stdscr.addstr(1, 0, "Press 'r' for red", curses.color_pair(6))
    stdscr.addstr(2, 0, "Press 'b' for blue", curses.color_pair(2))
    stdscr.addstr(3, 0, "Press 'g' for green", curses.color_pair(5))
    stdscr.addstr(4, 0, "Press 'y' for yellow", curses.color_pair(4))
    stdscr.addstr(5, 0, "Press 'space' to start")

    stdscr.refresh()
    
    while True:
        key = stdscr.getch()
        if key == ord(' '):
            break
        elif key == ord('r'):
            color = Color.RED.value
            break
        elif key == ord('b'):
            color = Color.BLUE.value
            break
        elif key == ord('g'):
            color = Color.GREEN.value
            break
        elif key == ord('y'):
            color = Color.YELLOW.value
            break
        
    return color
    
if __name__ == "__main__":
    curses.wrapper(main)
    # Clear screen

