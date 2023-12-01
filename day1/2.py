# import file 
raw_file = open("calibration.txt", "r")
lines = raw_file.readlines()

values = []
digit_words = ["one", "two", "three", "four", "five", "six", "seven", "eight", "nine"]

for line in lines:

    first_digit = 0;
    last_digit = 0;

    # front to back
    first_digit_found = False
    for i in range(0, len(line)): 
        if(first_digit_found == False):
            if line[i].isdigit():
                first_digit = line[i]
                first_digit_found = True
                break
            else:
                for j in range(0, 9):
                    if line[i:i+len(digit_words[j])] == digit_words[j]:
                        first_digit = str(j+1)
                        first_digit_found = True
                        break
 
    # back to front
    last_digit_found = False
    for i in reversed(range(0, len(line))): 
        if(last_digit_found == False):
            if line[i].isdigit():
                last_digit = line[i]
                last_digit_found = True
                break
            else:
                for j in range(0, 9):
                    if line[i:i+len(digit_words[j])] == digit_words[j]:
                        last_digit = str(j+1)
                        last_digit_found = True
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
