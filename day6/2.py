# import file 
raw_file = open("races.txt", "r")
lines = raw_file.readlines()

# process data
time = int("".join(lines[0].split(":")[1].split()))
distance = int("".join(lines[1].split(":")[1].split()))
count = 0

#check all possible times
for button_time in range(0, time):
    distance_travelled = (time - button_time) * button_time
    if distance_travelled > distance: count += 1
    
print(count)