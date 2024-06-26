import numpy as np
print('Welcome to Rock Paper Scissors!')
user_play = input('Please enter Rock, Paper, or Scissors!\n')

# Rules: Rock beats scissors, scissors beats paper, paper beats rock
def computer():
    pc_choices = ['Rock', 'Paper', 'Scissors']
    pc_play = np.random.choice(pc_choices)
    return pc_play

if user_play.lower() == 'rock' or user_play == 'Rock':
    if computer() == 'Rock':
        print('The game is a draw, please play again!')
        # Nu nog hier maken dat je dan opnieuw begint, moet met een def dan kan je hem opnieuw aanroepen
    if computer() == 'Scissors':
        result = input('You have won, do you want to play again? [Y/N]\n')
        if result == 'Y':
            print('Play again')
            # Nu nog hier maken dat je dan opnieuw begint, moet met een def dan kan je hem opnieuw aanroepen
        if result == 'N':
            print('Thanks for playing, have a good day!')
    if computer() == 'Paper':
        result = input('You have unfortunately lost, do you want to play again? [Y/N]\n')
        if result == 'Y':
            print('Play again')
            # Nu nog hier maken dat je dan opnieuw begint, moet met een def dan kan je hem opnieuw aanroepen
        if result == 'N':
            print('Thanks for playing, have a good day!')
if user_play.lower() == 'sciccors' or user_play == 'Scissors':
    if computer() == 'Scissors':
        print('The game is a draw, please play again!')
        # Nu nog hier maken dat je dan opnieuw begint, moet met een def dan kan je hem opnieuw aanroepen
    if computer() == 'Paper':
        result = input('You have won, do you want to play again? [Y/N]\n')
        if result == 'Y':
            print('Play again')
            # Nu nog hier maken dat je dan opnieuw begint, moet met een def dan kan je hem opnieuw aanroepen
        if result == 'N':
            print('Thanks for playing, have a good day!')
    if computer() == 'Rock':
        result = input('You have unfortunately lost, do you want to play again? [Y/N]\n')
        if result == 'Y':
            print('Play again')
            # Nu nog hier maken dat je dan opnieuw begint, moet met een def dan kan je hem opnieuw aanroepen
        if result == 'N':
            print('Thanks for playing, have a good day!')
if user_play.lower() == 'paper' or user_play == 'Paper':
    if computer() == 'Paper':
        print('The game is a draw, please play again!')
        # Nu nog hier maken dat je dan opnieuw begint, moet met een def dan kan je hem opnieuw aanroepen
    if computer() == 'Rock':
        result = input('You have won, do you want to play again? [Y/N]\n')
        if result == 'Y':
            print('Play again')
            # Nu nog hier maken dat je dan opnieuw begint, moet met een def dan kan je hem opnieuw aanroepen
        if result == 'N':
            print('Thanks for playing, have a good day!')
    if computer() == 'Scissors':
        result = input('You have unfortunately lost, do you want to play again? [Y/N]\n')
        if result == 'Y':
            print('Play again')
            # Nu nog hier maken dat je dan opnieuw begint, moet met een def dan kan je hem opnieuw aanroepen
        if result == 'N':
            print('Thanks for playing, have a good day!')