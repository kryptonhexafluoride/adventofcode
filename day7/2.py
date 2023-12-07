# import file 
raw_file = open("hands.txt", "r")
lines = raw_file.readlines()

# this is to make sorting possible 
def comparator_key(hand):
    # the letters VERY INCONVENIENTLY not in alphabetical order
    # so we will fix that with some contrived bullshit
    # jokers are 1s because they suck and they go last
    hand = hand.replace('A', 'Z').replace('K', 'Y').replace('Q', 'X').replace('T', 'W').replace('J', '1')
    frequencies = {c:hand.count(c) for c in hand}

    # joker shenanigans
    if '1' in frequencies.keys() and len(frequencies.keys()) > 1:
        num_jokers = frequencies['1']
        frequencies.pop('1')
        # add the number of jokers to the largest number in the dict 
        # in case of ties, add the joker count to the higher card's count
        # we do not modify the hand itself, because we need that for tiebreakers
        max_freq = max(list(frequencies.values()))
        jokers_are_this_card_now = max([card for card,freq in frequencies.items() if freq == max_freq])
        print(jokers_are_this_card_now)
        frequencies[jokers_are_this_card_now] += num_jokers

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
print(sorted_hands)

total_rank = 0
for i in range(0, len(sorted_hands)):
    total_rank += ((hands[sorted_hands[i]]) * (i+1))

print(total_rank)