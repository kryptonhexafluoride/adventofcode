# import file 
raw_file = open("almanac.txt", "r")
lines = raw_file.readlines()

# annoying as hell string parsing
seeds = [int(str) for str in lines[0].split(": ")[1].split()]

# each map is gonna be an array arrays of 3 element arrays (screaming)
# we start from 3 on this for loop to leave out the initial stuff 
maps = []
map_filler_array = []
for i in range(3, len(lines)):
    if lines[i] == '\n':
        maps.append(map_filler_array)
        map_filler_array = []
    elif ':' not in lines[i]:
        map_filler_array.append([int(str) for str in lines[i].strip().split()])
maps.append(map_filler_array)
    
# find the location for each seed 
locations = []
for seed in seeds: 
    working_num = seed
    for map in maps:
        for range in map: 
            if (working_num >= range[1]) and (working_num <= range[1] + range[2]):
                working_num = range[0] + (working_num-range[1])
                break
    locations.append(working_num)

print(min(locations))