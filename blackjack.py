import numpy as np
from collections import Counter
colors = ['Spades', 'Clubs', 'Diamonds', 'Hearts']
numbers = ['2', '3', '4', '5', '6', '7', '8', '9', '10', '11', '12', '13', '14']
pictures = {'11' : 'Jack', '12' : 'Queen', '13' : 'King', '14' : 'Ace'}
cards_dict = {}
for i in range(0, 52):
    color = np.random.choice(colors)
    number = np.random.choice(numbers)
    if number in pictures:
        number = pictures.get(number)
    card = f'{color} {number}'
    if card not in cards_dict.values():
        cards_dict[i] = card
        print(card)

    else:
        print(f'{card} is already in the dictionary')
        while card in cards_dict.values():
            color = np.random.choice(colors)
            number = np.random.choice(numbers)
            if number in pictures:
                number = pictures.get(number)
            card = f'{color} {number}'
            if card not in cards_dict.values():
                cards_dict[i] = card
                print(card)
                break

print(cards_dict)