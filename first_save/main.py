import functions
clear()
# Calculate amount of weird substance needed for mazes
# Mazes require weird substance equal to world size. Doubles with every level up
# after the first unlock.
maze_level = num_unlocked(Unlocks.Mazes)
substance_needed = get_world_size() * (2**maze_level-1)

# Code to farm field
hay = 0
bush = 0
tree = 1
carrot = 5
pumpkin = 5
sunflower = 1

while True:
    functions.farm_field(hay, bush, tree, carrot, pumpkin, sunflower)















