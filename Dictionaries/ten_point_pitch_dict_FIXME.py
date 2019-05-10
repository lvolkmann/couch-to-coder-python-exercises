"""
Provided below is a dictionary for 10 point pitch {card : points}
Write a program to build a new dictionary such that the points are the key and the values are the cards {points: [card1, card2]}
"""

card_dict = {'3': 3, '10': 1, '5': 0, '9': 0, '7': 0, '8': 0, '6': 0, '2': 1, '4': 0, 'Ace' : 1, 'King' : 0, 'Queen' : 0, 'OnJack' : 1, 'OffJack' : 1, 'HiJoker' : 1, 'LoJoker' : 1}

new_dict= {} #by points

for key, value in card_dict.items():
        if value in new_dict:
            new_dict[value].append(key)
        else:
            new_dict[value] = [key]

for key, value in new_dict.items():
    print(key, value)