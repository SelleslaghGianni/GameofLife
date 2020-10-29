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

print(random_state(20, 20))
