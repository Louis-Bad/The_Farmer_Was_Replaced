import functions

while True:
    for i in range(get_world_size()):
        functions.pumpkin_patch()
        harvest()
        move(North)
    move(East)


















