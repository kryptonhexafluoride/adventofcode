from itertools import cycle

# import file 
raw_file = open("directions.txt", "r")
lines = raw_file.readlines()

# process strings 
left_right = lines[0].strip()

instructions = {}
for i in range(2, len(lines)):
    split = lines[i].split(" = ")
    instructions[split[0]] = [split[1][1:4], split[1][6:9]]

current_location = "AAA"
count = 0
for direction in cycle(left_right):
    if current_location == "ZZZ":
        break
    count += 1
    match direction:
        case 'R':
            current_location = instructions[current_location][1]
        case 'L':
            current_location = instructions[current_location][0]

print(count)