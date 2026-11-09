# ----------
# This file will contain a list of useful code I want to reuse.
# ----------


def float_to_int(num):
    # Function will take a number and return just the integer value
    return num // 1



def tile_info():
    # Function will return all the information about the current tile.

    coords = (get_pos_x(), get_pos_y()) 
    ground = get_ground_type()
    plant = get_entity_type()
    
    return {"coords":coords, "ground":ground, "plant":plant} 

def get_tile(direction):
    # Function will move to an adjacent tile, read that tiles info and move back.
    if direction == North:
        move(North)
        info = tile_info()
        move(South)

    elif direction == East:
        move(East)
        info = tile_info()
        move(West)

    elif direction == South: 
        move(South)
        info = tile_info()
        move(North)

    elif direction == West: 
        move(West)
        info = tile_info()
        move(East)

    else:
        info = tile_info()

    return info


def farm_field(hay=2, bush=0, tree=2, carrot=4, pumpkin=0):
    # Farm specific items across specified columns and patches.
    # Function takes integers for each arguement, representing the number of
    # columns that should be assigned to that plant. 
    # Will be expanded to also allow for the assignment of square areas to plants.


    # Create a list of n column numbers, where n is the size of the world
    all_cols = list(range(get_world_size()))

    col_allocation = {"hay_cols":hay,
                      "bush_cols":bush,
                      "tree_cols":tree, 
                      "carrot_cols":carrot,
                      "pumpkin_cols":pumpkin}


    
    
    # The for loop will take the col_allocation dict above and convert the 
    # values representing the number of columns to be allocated to that plant 
    # into a corresponding list of columns that the plant will occupy on the farm.
    start = 0
    for key in col_allocation:
        # Assign a list of columns to each plant
        stop = start + col_allocation[key]
        col_allocation[key] = all_cols[start:stop]

        # Update the starting column for the next plant 
        start = stop

    

    # For loop will farm each plant across the assigned columns
    for col in range(get_world_size()):

        # Farm hay
        if get_pos_x() in col_allocation["hay_cols"]:
            for i in range(get_world_size()):
                harvest()
                move(North)
                
            move(East)

        # Farm bush
        elif get_pos_x() in col_allocation["bush_cols"]:
            for i in range(get_world_size()):
                harvest()
                plant(Entities.Bush)
                move(North)
                
            move(East)
        
        # Farm trees
        elif get_pos_x() in col_allocation["tree_cols"]:
            for i in range(get_world_size()):
                if (get_pos_x() in col_allocation["tree_cols"] and get_pos_y() % 2 == 0):
                    harvest()
                    plant(Entities.Tree)
                    move(North)
                    move(East)
                
                elif get_pos_x() in col_allocation["tree_cols"] and get_pos_y() % 2 != 0:
                    harvest()
                    plant(Entities.Tree)
                    move(North)
                    move(West)

            if get_pos_x() == col_allocation["tree_cols"][0]:
                move(East)
                move(East)
            elif get_pos_x() == col_allocation["tree_cols"][1]:
                move(East)
            
        # Farm carrots		
        elif get_pos_x() in col_allocation["carrot_cols"]:
            for i in range(get_world_size()):
                if get_ground_type() == Grounds.Soil:
                    harvest()
                    plant(Entities.Carrot)
                    move(North)

                else:
                    harvest()
                    till()
                    plant(Entities.Carrot)
                    move(North)

            move(East)
    
    
    # ----- UNDER CONSTRUCTION -----
    # Farm mega pumpkin	
    num_passes = 0
    for epoch in range(num_passes): 
        for col in range(get_world_size()):
            for row in range(get_world_size()):
            
                if get_ground_type() == Grounds.Grassland:
                    harvest()
                    till()
                    plant(Entities.Pumpkin)
                    move(North)
                elif get_ground_type() == Grounds.Soil and get_entity_type() != Entities.Pumpkin:
                    harvest()
                    plant(Entities.Pumpkin)
                    move(North)
                elif get_ground_type() == Grounds.Soil and get_entity_type() == Entities.Pumpkin:
                    move(North)

            move(East)
    harvest()
















# Plant/Harvest specific items across specified columns before moving to next col
# Grass for the first column
def farm_field_old():
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
# def get_coords(start=[0,0], size=get_world_size()):
#     x_coords = [start[0]] 
#     y_coords = [start[1]]
# 
#     for i in range(size):
#         x_coords.append(start[0] += 1)
#         y_coords.append(start[1] += 1)
# 
#     return x_coords, y_coords








# UNDER CONSTRUCTION
# # Plant pumpkins across a specified patch size and location 
# def pumpkin_patch(start=[0,0], size=get_world_size(), cycles=3):
#     x_coords, y_coords = get_coords(start, size)
    
#     while get_pos_x() in x_coords and get_pos_y in y_coords:
#         if get_entity_type() == Entities.Pumpkin and not can_harvest():
#             harvest()
#             plant(Entities.Pumpkin)
#             move(North)
#         elif get_ground_type() == Grounds.Grassland:
#             till()
#             plant(Entities.Pumpkin)
#             move(North)
#         elif get_ground_type() == Grounds.Soil:
#             plant(Entities.Pumpkin)
#             move(North)









