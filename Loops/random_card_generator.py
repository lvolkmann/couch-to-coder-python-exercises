"""
Write a program to do the following:
	Build a deck of cards in the following form => suit value
		Hint: use for loops
	This deck should exist as a series of strings in a list ["H7", "CQ",...]
	If time:
		Draw a random card from the deck
		Devise a loop to draw two random cards and see if they're a match
		Keep track of number of tries
	If you want to go crazy:
		Create a loop that finds the average number of tries over n trials
"""

# import modules
import random

# Initialize list of possible suits
suits = ['H', 'D', 'S', 'C']

# Intialize list of possible values
values = ['A', 'K', 'Q', 'J']
for num in range(1,11):
	values.append(str(num))

# Intialize list of possible cards
cards = []
for suit in suits:
	for val in values:
		cards.append(suit + " " + val)

# Draw random card
print(cards[random.randint(1,52)])

# Card Match Extension
card_1 = 0
card_2 = 1
count = 0

# Note card_1 and card_2 initialized to 0 and 1 so we could enter into the loop
while(card_1 != card_2):
	count += 1
	card_1 = cards[random.randint(1,52)]
	card_2 = cards[random.randint(1,52)]
print(card_1, card_2, count)