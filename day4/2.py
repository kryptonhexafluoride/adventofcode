# import file 
raw_file = open("scratchcards.txt", "r")
lines = raw_file.readlines()

cards = []

for line in lines:
    line = line[0:len(line)-1].split(": ")[1]
    cards.append(line.split(" | "))

# this is an array now so we can track how many of each card we have
# we start with only 1 of EACH card
count = [1]*len(lines)

# for each card, check if the 2nd part contains any numbers from the 1st part 
for card_index in range(0, len(cards)): 
    temp_count = 0
    card = cards[card_index]
    winning_numbers = card[0].split(' ')
    our_numbers = card[1].split(' ')
    for number in winning_numbers:
        if(number in our_numbers) and (number != ''): 
            temp_count += 1

    # for all the cards that are temp_count away from the current card,
    # add 1 to their count a number of times equal to the count of the current card. 
    # ...or just add the count of the current card to it lol 
    for i in range(0, temp_count):
        count[1+i+card_index] += count[card_index]

sum = 0
for c in count:
    sum += c

print(count)
print(sum)

