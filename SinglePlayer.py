import curses

from Color import Color, init_foreground_colors, init_combined_colors
from Game import Game  
from Tile import Tile

def main(stdscr):
    
    # Curses Setup
    curses.curs_set(0)
    stdscr.keypad(True)
    stdscr.clear()
    
    # Initialize colors
    color_map = init_foreground_colors(curses)

    print_welcome_message(stdscr, color_map)
    no_of_players = select_no_of_players(stdscr, color_map)

    # Initial dot position
    x = 0
    y = 0
    tile_index = 0
    turn = 0
    
    game = Game(curses)
    game.init_game()
    grid = game.grid
    
    chosen_players = []

    # list of colors from game players
    player_colors = [Color(player.color) for player in game.players]

    # Pre-Game Screens
    for i in range(no_of_players):
        chosen_color = print_choose_color(stdscr , player_colors, curses)
        player_colors.remove(Color(chosen_color))
        chosen_player = list(filter(lambda player: player.color == chosen_color, game.players))[0]
        chosen_players.append(chosen_player)

    # prepare start tiles and list of other players            
    active_players = game.players.copy()
    curr_player_i = 0
    
    stdscr.clear()
    
    while True:

        curr_player = active_players[curr_player_i]
        
        # move_possible = game.is_move_possible(curr_player, grid, turn)
        next_move = game.get_possible_move(curr_player, grid, turn)
                            
        if next_move is not None:
            if curr_player in chosen_players:
                if turn < 4:
                    x, y = grid.determine_start_position(curr_player.color)
                i, tile_matrix = curr_player.hand[tile_index]

                local_turn = local_player_turn(stdscr, curses, curr_player.color, x, y, tile_index, grid, curr_player, tile_matrix, turn)
                if local_turn is None:
                    return
                x, y, tile_index = local_turn
            else:
                handtile = curr_player.hand[0]
                curr_player.do_move(grid, next_move[1], next_move[0], next_move[2], next_move[3])
        else:    
            active_players.remove(curr_player)
            grid.print_notification(stdscr, "Player " + curr_player.name + " has no more moves")
        
        color_map = init_combined_colors(curses)
        grid.print_player_bar(stdscr, color_map, game.players, active_players, curr_player_i)
        grid.print_grid_overlay_stdscr(stdscr, curses)
        stdscr.refresh()
        
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


def local_player_turn(stdscr, curs, chosen_color, x, y, tile_index, grid, chosen_player, tile_matrix, turn):
    move_done = False
    while not move_done:
        
        # # overflow protection
        x = min(x, grid.size - len(tile_matrix))
        y = min(y, grid.size - len(tile_matrix[0]))
        
        start_pos = grid.determine_start_position(chosen_color)

        tile_correct = False
        tile_correct = (turn < 4 and grid.matches_start_position(start_pos, (x,y),tile_matrix)) \
        or ((grid.tile_fits(chosen_color, (x,y), tile_matrix))
            and grid.color_correct(chosen_color, (x,y), tile_matrix)
            and grid.connection_possibly_correct(chosen_color, (x,y), tile_matrix)
            )
        if tile_correct:
            color = chosen_color
        else:
            color = Color.HIGHLIGHT.value

        # Draw the dot at the current position
        grid.print_grid_overlay_stdscr(stdscr, curs, (x, y), tile_matrix, color)

        # Refresh the screen
        stdscr.refresh()

        # Get user input
        key = stdscr.getch()

        # Move the dot based on the key input
        if key == curses.KEY_LEFT or key == ord('a'):
            y = max(0, y - 1)
        elif key == curses.KEY_RIGHT or key == ord('d'):
            y = min(curses.COLS - 1, y + 1)
        elif key == curses.KEY_UP or key == ord('w'):
            x = max(0, x - 1)
        elif key == curses.KEY_DOWN or key == ord('s'):
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
            return None

    return (x,y, tile_index)
        
        
        
def print_welcome_message(stdscr, color_map):
    
    stdscr.clear()
    
    print_arr = [
        ["Welcome to B L O K U S!", Color.YELLOW],
        ["Place as many tiles as possible to win", Color.WHITE],
        ["", Color.WHITE],
        ["Controls", Color.YELLOW],
        ["Use the arrow keys or w,a,s,d to move the tile", Color.WHITE],
        ["Press 'm' to mirror the tile", Color.WHITE],
        ["Press 'r' to rotate the tile", Color.WHITE],
        ["Press 'Space' to place the tile", Color.WHITE],
        ["Press 'y' to select the previous tile", Color.WHITE],
        ["Press 'x' to select the next tile", Color.WHITE],
        ["", Color.WHITE],
        ["Press 'q' to quit", Color.RED],
        ["Press 'Space' to start", Color.GREEN]
    ]
    
    for i, (text, color) in enumerate(print_arr):
        stdscr.addstr(i, 0, text, color_map.get(color.value))
       
    stdscr.refresh()
    
    while True:
        key = stdscr.getch()
        if key == ord(' '):
            break
    
def print_choose_color(stdscr, available_colors, curs):
    
    stdscr.clear()
    
    color_map = init_foreground_colors(curs)
    
    stdscr.addstr(0, 0, "Choose a color:", color_map.get(Color.YELLOW.value))
    
    color_key_map = {
        Color.RED: 'r',
        Color.BLUE: 'b',
        Color.GREEN: 'g',
        Color.YELLOW: 'y'
    }
    
    for i, color in enumerate(available_colors):
        key = color_key_map.get(color, '')
        full_color = Color(color)
        if key:
            stdscr.addstr(i + 1, 0, f"Press '{key}' for {full_color.name.lower()}", color_map.get(full_color.value))
    
    stdscr.addstr(5, 0, "Press 'space' to start", color_map.get(Color.GREEN.value))

    stdscr.refresh()
    
    while True:
        key = stdscr.getch()
        if key == ord(' '):
            color = available_colors[0].value
            break
        elif key == ord('r') and Color.RED in available_colors:
            color = Color.RED.value
            break
        elif key == ord('b') and Color.BLUE in available_colors:
            color = Color.BLUE.value
            break
        elif key == ord('g') and Color.GREEN in available_colors:
            color = Color.GREEN.value
            break
        elif key == ord('y') and Color.YELLOW in available_colors:
            color = Color.YELLOW.value
            break
        
    return color

def select_no_of_players(stdscr, color_map):
    stdscr.clear()
    
    num_players = 1
    
    print_arr = [
        ["Select number of players:", Color.YELLOW],
        ["Press '0' for 0 players", Color.WHITE],
        ["Press '1' for 1 player (default)", Color.WHITE],
        ["Press '2' for 2 players", Color.WHITE],
        ["Press '3' for 3 players", Color.WHITE],
        ["Press '4' for 4 players", Color.WHITE],
        ["Press 'space' to continue with default (1 player)", Color.GREEN]
    ]
    
    for i, (text, color) in enumerate(print_arr):
        stdscr.addstr(i, 0, text, color_map.get(color.value))
    
    stdscr.refresh()
    
    while True:
        key = stdscr.getch()
        if key == ord(' '):
            num_players = 1
            break
        elif key == ord('0'):
            num_players = 0
            break
        elif key == ord('1'):
            num_players = 1
            break
        elif key == ord('2'):
            num_players = 2
            break
        elif key == ord('3'):
            num_players = 3
            break
        elif key == ord('4'):
            num_players = 4
            break
    
    return num_players
    
if __name__ == "__main__":
    curses.wrapper(main)
    # Clear screen

