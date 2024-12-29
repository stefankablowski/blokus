import curses

from Color import Color
from Game import Game  
from Tile import Tile

def main(stdscr):
    
    # Pre-Game Screens
    print_welcome_message(stdscr)
    chosen_color = print_choose_color(stdscr)

    # Initial dot position
    x = 0
    y = 0
    tile_index = 0
    turn = 0
    
    game = Game()
    game.init_game()
    grid = game.grid
    
    chosen_player = [player for player in game.players if player.color == chosen_color][0]
    
    i, tile_matrix = chosen_player.hand[tile_index]

    # Hide the cursor
    curses.curs_set(0)
    stdscr.clear()
    
    # prepare start tiles and list of other players
    for player in game.players:
        if player != chosen_player:
            player.play_start_tile(game.grid, player.hand.pop(0), player.color)
    active_players = game.players.copy()
    curr_player_i = 0
    
    while True:

        curr_player = active_players[curr_player_i]
        
        move_possible = False
        # check if the current player can do possible moves
        if turn > 0:
            for handtile in curr_player.hand:
                placed = False
                for x_new in range(grid.size):
                    for y_new in range(grid.size):
                        if curr_player.play_tile(grid, (x_new,y_new), handtile, False):
                            placed = True
                            move_possible = True
                            break
                    if placed:
                        break
                if placed:
                        break
        else:
            move_possible = True
                    
        if move_possible:
            if curr_player == chosen_player:
                grid.print_player_bar(stdscr, game.players, active_players, curr_player_i)
                i, tile_matrix = chosen_player.hand[tile_index]

                x, y, tile_index = local_player_turn(stdscr, chosen_color, x, y, tile_index, grid, chosen_player, tile_matrix, turn)
            else:
                handtile = curr_player.hand.pop(0)
                placed = False
                for x_new in range(grid.size):
                    for y_new in range(grid.size):
                        if curr_player.play_tile(grid, (x_new,y_new), handtile):
                            placed = True
                            break
                    if placed:
                        break
        else:    
            active_players.remove(curr_player)
            grid.print_notification(stdscr, "Player " + curr_player.name + " has no more moves")
                
        turn += 1
        
        # End of Game Condition
        if len(active_players) == 0:
            break
        curr_player_i = (curr_player_i + 1) % len(active_players)

    winner = game.determine_winner()
    print_end_screen(stdscr, winner, grid)
    
    while True:
        key = stdscr.getch()
        if key == ord('q'):
            break

def print_end_screen(stdscr, player, grid):
    color_map = grid.color_map
    bg_color = color_map.get(player.color)
    stdscr.addstr(10, 0, f"{player.name} is the winner!", bg_color)
    stdscr.addstr(11, 0, "Press 'q' to exit.", bg_color)
    stdscr.refresh()


def local_player_turn(stdscr, chosen_color, x, y, tile_index, grid, chosen_player, tile_matrix, turn):
    move_done = False
    while not move_done:
        
        # # overflow protection
        x = min(x, grid.size - len(tile_matrix))
        y = min(y, grid.size - len(tile_matrix[0]))

        tile_correct = False
        tile_correct = (turn == 0 and grid.matches_start_position((0, 0), (x,y),tile_matrix)) \
        or ((grid.tile_fits(chosen_color, (x,y), tile_matrix))
            and grid.color_correct(chosen_color, (x,y), tile_matrix)
            and grid.connection_possibly_correct(chosen_color, (x,y), tile_matrix)
            )
        if tile_correct:
            color = chosen_color
        else:
            color = Color.HIGHLIGHT.value

        # Draw the dot at the current position
        grid.print_grid_overlay_stdscr(stdscr, (x, y), tile_matrix, color)

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
        elif key == ord('r'):
            tile_matrix = Tile.rotate_tile(tile_matrix, 1)
        elif key == ord('l'):
            tile_matrix = Tile.rotate_tile(tile_matrix, 3)
        elif key == ord(' '):
            if not tile_correct:
                continue
            grid.add_tile(chosen_color, (x, y), tile_index, tile_matrix)
            # update to a different tile
            prev_tile_index = tile_index
            chosen_player.hand.pop(tile_index)
            tile_index = min(len(chosen_player.hand) - 1, prev_tile_index)
            move_done = True
        # if key is x then decrement tile index but not below 0
        elif key == ord('y'):
            tile_index = max(0, tile_index - 1)
            i, tile_matrix = chosen_player.hand[tile_index]
        # if key is y then increment tile index but not above the length of the hand
        elif key == ord('x'):
            tile_index = min(len(chosen_player.hand) - 1, tile_index + 1)
            i, tile_matrix = chosen_player.hand[tile_index]
        # if key is m then mirror the tile
        elif key == ord('m'):
            tile_matrix = Tile.mirror_tile(tile_matrix, vertical=True)
            
        elif key == ord('q'):
            break

    return (x,y, tile_index)
        
        
        
def print_welcome_message(stdscr):
    
    stdscr.clear()
    
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
    
    stdscr.clear()
    
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

