# This file will contain a list of useful code I want to reuse.

# Plant/Harvest specific items across specified columns before moving to next col
# Grass for the first column
def farm_field():
	while True:
		if get_pos_x() == 0:
			for i in range(get_world_size()):
				harvest()
				move(North)
			move(East)

		# Wood across columns 2, 3, 4
		elif get_pos_x() in [1, 2, 3, 4, 5, 6]:
			for i in range(get_world_size()):
				harvest()
				plant(Entities.bush)
				move(North)
			move(East)

		# Carrots across the remaining columns
		else:
			for i in range(get_world_size()):
				if get_entity_type() == Entities.Carrot:
					harvest()
					plant(Entities.Carrot)
					move(North)
				elif get_ground_type() == Grounds.Grassland:
					till()
					plant(Entities.Carrot)
					move(North)
				elif get_ground_type() == Grounds.Soil:
					plant(Entities.Carrot)
					move(North)

			move(East)
		


# Function will take in a start coordinate and a size then return a dictionary 
# with 'x' and 'y' as the keys and the values being a list of values.
# This list of values will represent a nxn section of the farm
def get_coords(start=[0,0], size=get_world_size()):
    x_coords = [start[0]] 
    y_coords = [start[1]]

    for i in range(size):
        x_coords.append(start[0] += 1)
        y_coords.append(start[1] += 1)

    return x_coords, y_coords








# UNDER CONSTRUCTION
# Plant pumpkins across a specified patch size and location 
def pumpkin_patch(start=[0,0], size=get_world_size(), cycles=3):
    x_coords, y_coords = get_coords(start, size)
    
    while get_pos_x() in x_coords and get_pos_y in y_coords:
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










# UNDER CONSTRUCTION
def tree_grass_col():
	pass