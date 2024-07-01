import numpy as np
import re
colors = ['Spades', 'Clubs', 'Diamonds', 'Hearts']
numbers = ['2', '3', '4', '5', '6', '7', '8', '9', '10', '11', '12', '13', '14']
pictures = {'11' : 'Jack', '12' : 'Queen', '13' : 'King', '14' : 'Ace'}
reverse_pictures = {v: k for k, v in pictures.items()}  # Reverse the pictures dictionary for easy lookup
dealt_cards_total = []
dealt_cards_player = []
dealt_cards_dealer = []

def make_deck():
    cards_dict = []
    for i in range(0, 52):
        color = np.random.choice(colors)
        number = np.random.choice(numbers)
        if number in pictures:
            number = pictures.get(number)
        card = f'{color} {number}'
        if card not in cards_dict:
            cards_dict.append(card)

        else:
            while card in cards_dict:
                color = np.random.choice(colors)
                number = np.random.choice(numbers)
                if number in pictures:
                    number = pictures.get(number)
                card = f'{color} {number}'
                if card not in cards_dict:
                    cards_dict.append(card)
                    break
    return cards_dict

def get_card_value(card_value):
    if card_value in reverse_pictures:
        if card_value == 'Ace':
            return 11
        else:
            return 10
    else:
        return (int(card_value))

def game(cards_dict):
    score_player = 0
    score_dealer = 0
    dealt_card_dealer = np.random.choice(cards_dict)
    while dealt_card_dealer in dealt_cards_total:
        dealt_card_dealer = np.random.choice(cards_dict)
    dealt_cards_total.append(dealt_card_dealer)
    card_value_dealer = re.findall(r'\d+|Jack|Queen|Ace|King', dealt_card_dealer)[0]
    score_dealer += get_card_value(card_value_dealer)
    dealt_cards_dealer.append(dealt_card_dealer) #The dealt card to the dealer is randomly chosen from the list of cards, then checked if its already dealt,
        # and then added to these 2 lists, containing all dealt cards and the player dealt cards, which is used to keep the score of the player.
    print(f'The card of the dealer is {dealt_card_dealer}. The dealer has a current score of {score_dealer}.')

    new_card_player = 'Y'
    while new_card_player == 'Y':
        dealt_card_player = np.random.choice(cards_dict)
        while dealt_card_player in dealt_cards_total:
            dealt_card_player = np.random.choice(cards_dict)
        dealt_cards_total.append(dealt_card_player)
        dealt_cards_player.append(dealt_card_player) #The dealt card to the player is randomly chosen from the list of cards, then checked if its already dealt,
        # and then added to these 2 lists, containing all dealt cards and the player dealt cards, which is used to keep the score of the player.
        card_value_player = re.findall(r'\d+|Jack|Queen|Ace|King', dealt_card_player)[0]
        score_player += get_card_value(card_value_player)

        print(f'The card you have been delt is {dealt_card_player}. Your current score is {score_player}.')
        if score_player == 21:
            print('Congratulations, you have won!')
            new_card_player = 'N'
            break
        if score_player > 21:
            print('You have unfortunately busted, please play again!')
            break
        new_card_player = input(f'Would you like to draw a new card? [Y/N]: ')
        if new_card_player == 'N':
            while score_dealer <= 17:
                while dealt_card_dealer in dealt_cards_total:
                    dealt_card_dealer = np.random.choice(cards_dict)
                dealt_cards_total.append(dealt_card_dealer)
                card_value_dealer = re.findall(r'\d+|Jack|Queen|Ace|King', dealt_card_dealer)[0]
                score_dealer += get_card_value(card_value_dealer)
                dealt_cards_dealer.append(dealt_card_dealer) #The dealt card to the dealer is randomly chosen from the list of cards, then checked if its already dealt,
                    # and then added to these 2 lists, containing all dealt cards and the player dealt cards, which is used to keep the score of the player.
                print(f'The card of the dealer is {dealt_card_dealer}. The dealer has a current score of {score_dealer}.')
            if score_dealer <= 21 and score_dealer >= score_player:
                print('Unfortunately the dealer has won, please play again!')
                break
            break
    return

def main():
    play_again = 'Y'
    while play_again.strip().upper() == 'Y':
        cards_dict = make_deck()
        game(cards_dict)
        play_again = input(f'Would you like to play again? [Y/N]: ').strip().upper()
    print('Thank you for playing!')

main()
# https://www.askpython.com/python/examples/blackjack-game-using-python