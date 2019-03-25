#my_dict = {"bob":12, "bill":11, "alice":13, "gene":14}
#print(my_dict)
#my_dict["paula"] = 27
#print(my_dict)

import random

names = ["Tim from accounting", "David Schwimmer", "Colonel Sanders", "Colonel Mustard", "Santa Clause", "Mrs. Pacman", "Ruth"]
candidates = []
for name in names:
    for x in range(random.randint(1,15)):
        candidates.append(name)

random.shuffle(candidates)

votes = {}

for cand in candidates:
    votes[cand] = votes.get(cand,0)+1

print(votes)

#Cards
values = ['Ace', 'King', 'Queen', 'Jack', '2', '3', '4', '5', '6', '7', '8', '9', '10']
card_dict = {'3': 3, '10': 1, '5': 0, '9': 0, '7': 0, '8': 0, '6': 0, '2': 1, '4': 0, 'Ace' : 1, 'King' : 0, 'Queen' : 0, 'OnJack' : 1, 'OffJack' : 1, 'HiJoker' : 1, 'LoJoker' : 1}

new_dict= {} #by points

for key, value in card_dict.items():
        if value in new_dict:
            new_dict[value].append(key)
        else:
            new_dict[value] = [key]

for key, value in new_dict.items():
    print(key, value)
