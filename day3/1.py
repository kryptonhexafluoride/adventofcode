# import file 
raw_file = open("schematic.txt", "r")
lines = raw_file.readlines()

sum = 0
engine_parts = []

# before doing ANYTHING else we are gonna find the engine parts
for x in range(0, len(lines)):
    for y in range(0, len(lines[x])-1):
        if (lines[x][y].isdigit() == False) and (lines[x][y] != '.'):
            engine_parts.append((x,y))

print(engine_parts)

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
                            sum += int(current_number)
                            print(current_number)
                            number_added = True
                            break

                # now that we have added the number, we clear it out 
                current_number = ''
        
print(sum)