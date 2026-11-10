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





def farm_hay_col():
    # Function will farm hay along a column.
    for i in range(get_world_size()):
        harvest()
        move(North)
        
    move(East)




def farm_bush_col():
    # Function will farm bushes along a column.
    for i in range(get_world_size()):
        harvest()
        plant(Entities.Bush)
        move(North)
        
    move(East)




def farm_tree_col():
    # Function will plant trees along a column ensuring that no trees are
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
    # Function will farm carrots along a column. Ensuring to till the land only
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



def farm_pumpkin_col(size=0):
    # Function will farm pumpkins along a column such that a square patch of 
    # pumpkins will be created, spanning the length of the columns assigned to 
    # farming pumpkins.
    # The rest of each column will be left as hay for now.
    # Pumpkins will not be harvested until the NxN patch is filled with a giant
    # pumpkin.


    for i in range(get_world_size()):
        # Pumpkins along column
        if get_pos_y() in list(range(size)):

            # Till if needed first
            if get_ground_type() == Grounds.Grassland:
                if get_pos_y() == 0:
                    harvest()
                    till()
                    plant(Entities.Pumpkin)
                    first_measure = measure()
                    move(North)
                else:
                    harvest()
                    till()
                    plant(Entities.Pumpkin)
                    move(North)

            # Plant pumpkin if tilled but currently no pumpkin there
            elif get_ground_type() == Grounds.Soil and not get_entity_type():
                if get_pos_y() == 0:
                    plant(Entities.Pumpkin)
                    first_measure = measure()
                    move(North)
                else:
                    plant(Entities.Pumpkin)
                    move(North)

            # Replace if there is a dead pumpkin
            elif get_entity_type() == Entities.Dead_Pumpkin:
                if get_pos_y() == 0:
                    harvest()
                    plant(Entities.Pumpkin)
                    first_measure = measure()
                    move(North)
                else:
                    harvest()
                    plant(Entities.Pumpkin)
                    move(North)

            # If there is a fully grown pumpkin, ignore unless mega pumpkin
            elif get_entity_type() == Entities.Pumpkin:
                if get_pos_y() == 0:
                    first_measure = measure()
                    move(North)
                elif get_pos_y() == (size-1):
                    if measure() == first_measure:
                        harvest()
                        move(North)
                    else:
                        move(North)
                else:
                    move(North)

        # Hay along the rest of the column
        else:
            harvest()
            move(North)


    move(East)




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
    # Farm specific items along specified columns and patches.
    # Function takes integers for each arguement, representing the number of
    # columns that should be assigned to that plant. 
    # Will be expanded to also allow for the assignment of square areas.

    # Dict of plants and columns they will be farmed on
    col_allocation = assign_cols(hay, bush, tree, carrot, pumpkin)

    # For loop will farm each plant along the assigned columns
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
    
        # Farm pumpkins        
        elif get_pos_x() in col_allocation["pumpkin_cols"]:
            pumpkin_size = len(col_allocation["pumpkin_cols"])
            farm_pumpkin_col(pumpkin_size)
    


