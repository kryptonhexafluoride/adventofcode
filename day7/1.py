# import file 
raw_file = open("hands.txt", "r")
lines = raw_file.readlines()

# this is to make sorting possible 
def comparator_key(hand):
    # the letters VERY INCONVENIENTLY not in alphabetical order
    # so we will fix that with some contrived bullshit
    hand = hand.replace('A', 'Z').replace('K', 'Y').replace('Q', 'X').replace('J', 'W').replace('T', 'V')
    frequencies = {c:hand.count(c) for c in hand}

    if len(frequencies) == 1:
        # five of a kind
        return '6' + hand
    
    if len(frequencies) == 2:
        # four of a kind
        if 4 in frequencies.values():
            return '5' + hand
        # full house
        return '4' + hand
    
    if len(frequencies) == 3:
        # three of a kind
        if 3 in frequencies.values():
            return '3' + hand
        # two pair
        return '2' + hand
    
    if len(frequencies) == 4:
        # one pair
        return '1' + hand
    
    # high card
    return '0' + hand

# format strings to be nice and pretty 
hands = {}
for line in lines:
    hands[line.split()[0]] = int(line.split()[1])

# sorting and math 
sorted_hands = sorted(hands.keys(), key=comparator_key)

total_rank = 0
for i in range(0, len(sorted_hands)):
    total_rank += ((hands[sorted_hands[i]]) * (i+1))

print(total_rank)