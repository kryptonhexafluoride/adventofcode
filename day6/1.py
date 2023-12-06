# import file 
raw_file = open("races.txt", "r")
lines = raw_file.readlines()

# process data
times = lines[0].split(":")[1].split()
distances = lines[1].split(":")[1].split()
product = 1

for index in range(0, len(times)):
    count = 0
    current_time = int(times[index])
    record_distance = int(distances[index])
    
    #check all possible times
    for button_time in range(0, current_time):
        distance_travelled = (current_time - button_time) * button_time
        if distance_travelled > record_distance: count += 1
    
    product *= count

print(product)