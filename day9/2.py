# import file 
raw_file = open("histories.txt", "r")
lines = raw_file.readlines()

# process data
histories = []
for l in lines:
    h = []
    for i in l.split():
        h.append(int(i))
    histories.append(h)

# find and store the difference bw subsequent numbers in array of arrays
# keep doing this till we get all 0s
# then add last number of current array to last number of previous array
def recursion_helper(history):
    if(history.count(0) == len(history)):
        return 0
    diffs = []
    for h in range(1, len(history)):
        diffs.append(history[h] - history[h-1])
    return history[0] - recursion_helper(diffs)

results = 0
for h in histories:
    results += recursion_helper(h)

print(results)

