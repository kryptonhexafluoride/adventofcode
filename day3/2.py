# import file 
raw_file = open("schematic.txt", "r")
lines = raw_file.readlines()

engine_parts = dict()

# before doing ANYTHING else we are gonna find the relevant engine parts
# this is a dict so we can keep track of adjacent numbers 
for x in range(0, len(lines)):
    for y in range(0, len(lines[x])-1):
        if (lines[x][y]) == '*':
            engine_parts[(x,y)]=[]

# now for the real problem solving.  
# iterate OVER each row 
for line_index in range(0, len(lines)):
    current_line = lines[line_index]
    current_number = ''

    # iterate WITHIN each row 
    for char_index in range (0, len(current_line)): 
        current_char = current_line[char_index] 

        # build a number 
        if(current_char.isdigit()): 
            current_number += current_char
        
        else: 
            # if we hit a non-number, 
            # then we know the current number is over 
            if(len(current_number) > 0): 
                # we need to prevent double counting
                number_added = False

                # backtrack and check for symbols
                for temp_line_index in range(line_index-1, line_index+2): 
                    for temp_char_index in range(char_index-(len(current_number)+1), char_index+1): 
                        if((temp_line_index, temp_char_index) in engine_parts) and number_added == False: 

                            # associate the number and engine part in our dict
                            engine_parts[(temp_line_index, temp_char_index)].append(current_number)
                            number_added = True
                            break

                # now that we have added the number, we clear it out 
                current_number = ''

# calculate final answer
sum = 0

for part in engine_parts.keys():
    if(len(engine_parts.get(part)) == 2):
        sum += int(engine_parts.get(part)[0]) * int(engine_parts.get(part)[1])

print(sum)
