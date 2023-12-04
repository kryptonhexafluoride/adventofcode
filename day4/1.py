# import file 
raw_file = open("scratchcards.txt", "r")
lines = raw_file.readlines()

cards = []

for line in lines:
    line = line[0:len(line)-1].split(": ")[1]
    cards.append(line.split(" | "))

# for each card, check if the 2nd part contains any numbers from the 1st part 

sum = 0
for card in cards: 
    count = 0
    winning_numbers = card[0].split(' ')
    our_numbers = card[1].split(' ')
    for number in winning_numbers:
        if(number in our_numbers) and (number != ''): 
            count += 1
    if(count > 0): 
        sum += 2 ** (count-1)

print(sum)

