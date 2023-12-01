# import file 
raw_file = open("calibration.txt", "r")
lines = raw_file.readlines()

values = []

for line in lines:

    first_digit = 0;
    last_digit = 0;

    # front to back
    for i in range(0, len(line)): 
        if line[i].isdigit():
            first_digit = line[i]
            break
 
    # back to front
    for i in reversed(range(0, len(line))): 
        if line[i].isdigit():
            last_digit = line[i]
            break

    # concatenate the 2 digits to make a number 
    num = first_digit + last_digit
    values.append(num)

# take the final sum 
print(values)
result = 0
for v in values:
    result += int(v) 

print(result)
