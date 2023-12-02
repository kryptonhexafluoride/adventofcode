# import file 
raw_file = open("cubes.txt", "r")
lines = raw_file.readlines()

sum = 0

# parse these gosh darn strings to make them PRETTY
for x in range(0, len(lines)):

    line = lines[x][lines[x].index(':')+2:len(lines[x])-1]
    draws = line.split('; ' );

    max_red = 0
    max_blue = 0
    max_green = 0

    for d in draws:
        colours = d.split(', ')
        for c in colours: 
            if "red" in c:
                if int(c[0:len(c)-3]) > max_red:
                    max_red = int(c[0:len(c)-3])
            elif "blue" in c:
                if int(c[0:len(c)-4]) > max_blue:
                    max_blue = int(c[0:len(c)-4])
            elif "green" in c:
                if int(c[0:len(c)-5]) > max_green:
                    max_green = int(c[0:len(c)-5])
        
    sum += max_red*max_green*max_blue

print(sum)

