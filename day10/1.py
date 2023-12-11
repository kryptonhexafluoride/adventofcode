from collections import defaultdict

# import file 
raw_file = open("pipes.txt", "r")
lines = raw_file.readlines()

# create a graph from the input 
graph = defaultdict(set)
animal_row = 0
animal_col = 0

for row in range(0, len(lines)):
    for col in range(0, len(lines[row])):
        char = lines[row][col]
        match(char):
            case '|':
                if row-1 in range(0, len(lines)):
                    graph[(row, col)].add((row-1, col))
                if row+1 in range(0, len(lines)):
                    graph[(row, col)].add((row+1, col))
            case '-':
                if col-1 in range(0, len(lines[0])):
                    graph[(row, col)].add((row, col-1))
                if col+1 in range(0, len(lines[0])):
                    graph[(row, col)].add((row, col+1))
            case 'L':
                if row-1 in range(0, len(lines)):
                    graph[(row, col)].add((row-1, col))
                if col+1 in range(0, len(lines[0])):
                    graph[(row, col)].add((row, col+1))
            case '7':
                if row+1 in range(0, len(lines)):
                    graph[(row, col)].add((row+1, col))
                if col-1 in range(0, len(lines[0])):
                    graph[(row, col)].add((row, col-1))
            case 'J':
                if row-1 in range(0, len(lines)):
                    graph[(row, col)].add((row-1, col))
                if col-1 in range(0, len(lines[0])):
                    graph[(row, col)].add((row, col-1))
            case 'F':
                if row+1 in range(0, len(lines)):
                    graph[(row, col)].add((row+1, col))
                if col+1 in range(0, len(lines[0])):
                    graph[(row, col)].add((row, col+1))
            case 'S':
                animal_row = row
                animal_col = col

# get rid of the periods, we don't need those here 
for row in range(0, len(lines)):
    for col in range(0, len(lines[row])):
        if(lines[row][col]) == '.' and (row, col) in graph.keys():
            graph.pop((row, col))

# find animal neighbours 
for (row, col) in list(graph.keys()): 
    if (animal_row, animal_col) in graph[(row, col)]:
        graph[(animal_row, animal_col)].add((row, col))

# walk along the main loop until we get back to the start 
s = []
visited = set()
s.append((animal_row, animal_col))
while len(s) > 0: 
    row, col = s.pop()
    if (row, col) not in visited:
        visited.add((row, col))
        for (neighbour_row, neighbour_col) in graph[(row, col)]:
            s.append((neighbour_row, neighbour_col))

print(int(len(visited)/2))