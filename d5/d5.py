seed_destination_map = {}
current_map = []

with open("input.txt", "r") as file:
    for line in file:
        line = line.strip()

        # if there is a semicolon it means we are either on the first line
        # defining seed to plant or that we are on a line that begins the 
        # description of a new map
        if ":" in line:
            
            # in the case we do not have any seed to plant we are at the first line
            # and we initialize it
            if seed_destination_map == {}:
                for num_seed in line.split(": ")[1].split(" "):
                    seed_destination_map[int(num_seed)] = int(num_seed)

            # in the other case we modify the values of our destinations with the map we
            # got in the previous section
            else:
                # we iterate through each seeds
                for k_seed in seed_destination_map:
                    # and through each destination range
                    for dest_range_start, source_range_start, range_lenght in current_map:
                        # if our destination is currently in the range then we apply it the modifications
                        if source_range_start <= seed_destination_map[k_seed] < source_range_start + range_lenght:
                            seed_destination_map[k_seed] = dest_range_start + (seed_destination_map[k_seed] - source_range_start)
                            # we only want to modify each destination once so we break out of the map for this seed
                            break
                
                # we reinitialize the map
                current_map = []
        
        # when we are not on a semicolon line we take the numbers and put them in our current map
        else:
            args = line.split(" ")
            if len(args) == 3:
                dest_range_start, source_range_start, range_lenght = args
                current_map.append((int(dest_range_start), int(source_range_start), int(range_lenght)))

    # as the file soes not end with a line conatining a semicolon we need to reapeat the operation once
    # to filter destinations one last time
    for k_seed in seed_destination_map:
        for dest_range_start, source_range_start, range_lenght in current_map:
            if source_range_start <= seed_destination_map[k_seed] < source_range_start + range_lenght:
                seed_destination_map[k_seed] = dest_range_start + (seed_destination_map[k_seed] - source_range_start)
                break

# we only take the minimum of the results
print(min(seed_destination_map.values()))