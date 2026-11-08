def pumpkin_patch(start=[1,1], size=4, cycles=3):
    if get_pos_x == start[0] and get_pos_y == start[1]:
        while cycles > 0:

            for col in range(size):
                for row in range(size):
                    if get_entity_type() == Entities.Pumpkin and not can_harvest():
                        harvest()
                        plant(Entities.Pumpkin)
                        move(North)
                    elif get_ground_type() == Grounds.Grassland:
                        till()
                        plant(Entities.Pumpkin)
                        move(North)
                    elif get_ground_type() == Grounds.Soil:
                        plant(Entities.Pumpkin)
                        move(North)

            cycles -= 1
        harvest()

    else:
        pass