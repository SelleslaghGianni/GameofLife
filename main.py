import random

LIVE = 1
DEAD = 0

def dead_state(width, height):
    """
    Parameters
    --------
    Width: Width of the board
    Height: Height of the board

    Returns
    --------
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
    state: a Game state

    Returns:
    The width of the input state
    """
    return len(state)

def state_height(state):
    """Get the height of the state.
    Params:
    state: a Game state
    
    Returns:
    The height of the input state"""
    return len(state[0])

def render(board_state):

    DISPLAY_AS = {
        DEAD: ' ',
        #Unicode for a filled in square.
        LIVE : u"\u2588"
    }

    lines = []
    for x in range(state_height(board_state)):
        line = ''
        for y in range(state_width(board_state)):
            line += DISPLAY_AS[board_state[x][y]] * 2
        lines.append(line)
    print("\n".join(lines))

render(random_state(20, 20))


