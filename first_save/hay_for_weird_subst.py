clear()
while True:
    for i in range(get_world_size()):
        if num_items(Items.Fertilizer) > 0:
            use_item(Items.Fertilizer)
            harvest()
            move(North)
        else:
            harvest()
            move(North)
            
    move(East)