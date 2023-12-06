# figure out how to make a mapping of maps -- convert first one into last one

# import file 
raw_file = open("almanac.txt", "r")
lines = raw_file.readlines()

# annoying as hell string parsing
initial_seeds = [int(str) for str in lines[0].split(": ")[1].split()]

# NAIVE SOLUTION BABY LETS GOOOOOO
seeds = []
for i in range(0, int(len(initial_seeds)/2)):
    for j in range(0, initial_seeds[(2*i)+1]):
        seeds.append(initial_seeds[2*i]+j)

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