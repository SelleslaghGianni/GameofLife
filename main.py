import random
import time

LIVE = 1
DEAD = 0

def dead_state(width, height):
    """
    Parameters
    -------
    Width: Width of the board
    Height: Height of the board

    Returns
    -------
    The board with the dimensions specified, all cells set to DEAD.
    """
    return [[DEAD for _ in range(height)] for _ in range(width)]

def random_state(width, height):
    """
    Parameters
    -------
    Width: width of the board
    Height: height of the board

    Returns
    -------
    A board with randomized 0's and 1's.
    """
    state = dead_state(width, height)

    for x in range(0, width):
        for y in range(0, height):
            random_number = random.random()
            if random_number >= 0.5:
                cell_state = LIVE
            else:
                cell_state = DEAD
            state[x][y] = cell_state

    return state

def state_width(state):
    """Get the width of the state.
    Params:
    -------
    state: a Game state

    Returns:
    -------
    The width of the input state
    """
    return len(state)

def state_height(state):
    """Get the height of the state.
    Params:
    -------
    state: a Game state
    
    Returns:
    -------
    The height of the input state"""
    return len(state[0])

def render(board_state):
    """Render function.

    Params:
    -------
    board_state: the state of the board.

    Returns:
    -------
    Nothing, this is just to print it pretty.
    """

    width = state_width(board_state)
    height = state_height(board_state)

    DISPLAY_AS = {
        DEAD: ' ',
        #Unicode for a filled in square.
        LIVE : u"\u2588"
    }

    lines = []
    for x in range(0, height):
        line = ''
        for y in range(0, width):
            line += DISPLAY_AS[board_state[x][y]] * 2
        lines.append(line)
    print("\n".join(lines))

def next_board_state(initial_state):
    width = state_width(initial_state)
    height = state_height(initial_state)
    next_state = dead_state(width, height)


    for x in range(0, width):
        for y in range(0, height):
            next_state[x][y] = next_cell_value((x, y), initial_state)

    return next_state

def next_cell_value(coords, state):
    width = state_width(state)
    height = state_height(state)
    x = coords[0]
    y = coords[1]
    count_live_neighbors = 0

    for x1 in range((x - 1), (x + 1) + 1):
        if x1 < 0 or x1 >= width:
            continue

        for y1 in range((y - 1), (y + 1) + 1):
            if y1 < 0 or y1 >= height:
                continue
            if x1 == x and y1 == y:
                continue

            if state[x1][y1] == LIVE:
                count_live_neighbors += 1
    
    if state[x][y] == LIVE:
        if count_live_neighbors <= 1:
            return DEAD
        elif count_live_neighbors <= 3:
            return LIVE
        else:
            return DEAD
    else:
        if count_live_neighbors == 3:
            return LIVE
        else:
            return DEAD


def run_forever(init_state):
    next_state = init_state
    while True:
        render(next_state)
        next_state = next_board_state(next_state)
        time.sleep(0.10)


if __name__ == "__main__":
    init_state = random_state(100, 100)
    run_forever(init_state)
