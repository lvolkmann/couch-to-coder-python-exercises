#import modules
import random

#Initialize list of possible suits
suits = ['H', 'D', 'S', 'C']

#Intialize list of possible values
values = ['A', 'K', 'Q', 'J']
for num in range(1,11):
	values.append(str(num))

#Intialize list of possible cards
cards = []
for suit in suits:
	for val in values:
		cards.append(suit + " " + val)

#Draw random card
print(cards[random.randint(1,52)])

#While loop extension
card_1 = 0
card_2 = 1
count = 0

while(card_1 != card_2):
	count += 1
	card_1 = cards[random.randint(1,52)]
	card_2 = cards[random.randint(1,52)]
print(card_1, card_2, count)
