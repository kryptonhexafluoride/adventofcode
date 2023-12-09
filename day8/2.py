from itertools import cycle
from math import lcm

# import file 
raw_file = open("directions.txt", "r")
lines = raw_file.readlines()

# process strings 
left_right = lines[0].strip()

instructions = {}
for i in range(2, len(lines)):
    split = lines[i].split(" = ")
    instructions[split[0]] = [split[1][1:4], split[1][6:9]]

# get all starting locations
current_locations = []
for location in instructions.keys():
    if(location[2]) == 'A': current_locations.append(location)

counts = []

for l in range(0, len(current_locations)):
    count = 0
    for direction in cycle(left_right):
        if current_locations[l][2] == 'Z':
            counts.append(count)
            break
        count += 1
        match direction:
            case 'R':
                current_locations[l] = instructions[current_locations[l]][1]
            case 'L':
                current_locations[l] = instructions[current_locations[l]][0]

print(lcm(*counts))