# import file 
raw_file = open("cubes.txt", "r")
lines = raw_file.readlines()

MAX_RED = 12
MAX_GREEN = 13
MAX_BLUE = 14
sum = 0

# parse these gosh darn strings to make them PRETTY
for x in range(0, len(lines)):
    game_id = x+1

    line = lines[x][lines[x].index(':')+2:len(lines[x])-1]
    draws = line.split('; ' );
    valid_game = True

    for d in draws:
        colours = d.split(', ')
        for c in colours: 
            if "red" in c:
                if int(c[0:len(c)-3]) > MAX_RED:
                    valid_game = False
            elif "blue" in c:
                if int(c[0:len(c)-4]) > MAX_BLUE:
                    valid_game = False
            elif "green" in c:
                if int(c[0:len(c)-5]) > MAX_GREEN:
                    valid_game = False
        
    if valid_game:
        sum += game_id

print(sum)

