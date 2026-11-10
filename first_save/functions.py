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




# ----- UNDER CONSTRUCTION -----
# Function will take in a start coordinate and a size then return a dictionary 
# with 'x' and 'y' as the keys and the values being a list of values.
# This list of values will represent a nxn section of the farm
def get_coords(start=[0,0], size=get_world_size()):
    x_coords = [start[0]] 
    y_coords = [start[1]]

    for i in range(size):
        x_coords.append()
        y_coords.append()

    return x_coords, y_coords



def farm_hay_col():
    # Function will farm hay across a column.
    for i in range(get_world_size()):
        harvest()
        move(North)
        
    move(East)




def farm_bush_col():
    # Function will farm bushes across a column.
    for i in range(get_world_size()):
        harvest()
        plant(Entities.Bush)
        move(North)
        
    move(East)




def farm_tree_col():
    # Function will plant trees across a column ensuring that no trees are
    # planted adjacent to one another (diagonal is fine).
    tree_left = get_tile(West)["plant"] == Entities.Tree
    tree_right = get_tile(East)["plant"] == Entities.Tree

    if tree_left or tree_right:
        for i in range(get_world_size()):
            if get_pos_y() % 2 == 0:
                harvest()
                move(North)
            else:
                harvest()
                plant(Entities.tree)
                move(North)
        move(East)

    else:
        for i in range(get_world_size()):
            if get_pos_y() % 2 == 0:
                harvest()
                plant(Entities.tree)
                move(North)
            else:
                harvest()
                move(North)
        move(East)




def farm_carrot_col():
    # Function will farm carrots across a column. Ensuring to till the land only
    # when needed.
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
def farm_pumpkin_patch():
    # Function will create an nxn patch and farm pumpkins within the patch.
    # Pumpkins will not be harvested until the patch is filled with a giant
    # pumpkin.
    pass



def assign_cols(hay=0, bush=0, tree=0, carrot=0, pumpkin=0):
    # Function will take in a number for each plant and then return a dict 
    # where each key-val pair will state the plant and the list of columns that
    # the plant will be farmed on.

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

    return col_allocation


def farm_field(hay=0, bush=0, tree=0, carrot=0, pumpkin=0):
    # Farm specific items across specified columns and patches.
    # Function takes integers for each arguement, representing the number of
    # columns that should be assigned to that plant. 
    # Will be expanded to also allow for the assignment of square areas.

    # Dict of plants and columns they will be farmed on
    col_allocation = assign_cols(hay, bush, tree, carrot, pumpkin)

    # For loop will farm each plant across the assigned columns
    for col in range(get_world_size()):

        # Farm hay
        if get_pos_x() in col_allocation["hay_cols"]:
            farm_hay_col()

        # Farm bush
        elif get_pos_x() in col_allocation["bush_cols"]:
            farm_bush_col()
        
        # Farm trees
        elif get_pos_x() in col_allocation["tree_cols"]:
            farm_tree_col()
            
        # Farm carrots        
        elif get_pos_x() in col_allocation["carrot_cols"]:
            farm_carrot_col()
    
    
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












