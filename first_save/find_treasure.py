from functions import *

def move_check(direction):

    if not move(direction):
        return False

    else:
        if direction == North:
            move(South)
            return True
        elif direction == East:
            move(West)
            return True
        elif direction == South:
            move(North)
            return True
        elif direction == West:
            move(East)
            return True


def available_moves():
    all_directions = {North:None, East:None, South:None, West:None}
    for direction in all_directions:
        all_directions[direction] = move_check(direction)

    return all_directions


while get_tile()["coords"] != measure():
    moves = available_moves()
    for direction in moves:
        if moves[direction]:
            move(direction)
        else:
            pass

harvest()