from random import randint, choice, sample, shuffle

print(randint(0, 100))

players = ['Max', 'Leo', 'Kate', 'Ron', 'Bill']
print(choice(players))

print(sample(players, 1))
cards = ['6', '7', '8', '9', 'T', 'J', 'Q', 'k', 'A']
print(cards)
shuffle(cards)
print(cards)