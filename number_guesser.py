import numpy as np
def game():
    count = 0
    found = False
    print('Welcome to the random number guesser.')
    computer_choice = np.random.randint(0, 101)
    while found != True:
        user_input = input('Enter your guess for the random number between 0 and 100:\n')
        if int(user_input) < computer_choice:
            print('The number you guessed is too low, please try again!')
            count += 1
        if int(user_input) > computer_choice:
            print('The number you guessed is too high, please try again!')
            count += 1
        if int(user_input) == computer_choice:
            print(f'Congratulations, you have found the number in {count} tries!')
            found = True
    return
game()