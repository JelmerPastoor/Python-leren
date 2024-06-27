import numpy as np
pc_choices = ['Rock', 'Paper', 'Scissors']

def game():
    print('Welcome to Rock Paper Scissors!')
    user_play = input('Please enter Rock, Paper, or Scissors!\n')
    pc_play = np.random.choice(pc_choices)
    if pc_play.lower() == user_play.lower():
        print('The game is a draw, please play again!')
    elif ((user_play.lower() == 'rock' and pc_play.lower() == 'paper') or 
          (user_play.lower() == 'paper' and pc_play.lower() == 'scissors') or 
          (user_play.lower() == 'scissors' and pc_play.lower() == 'rock')):
        print('You have unfortunately lost, please play again!')
    if ((user_play.lower() == 'rock' and pc_play.lower() == 'scissors') or 
          (user_play.lower() == 'paper' and pc_play.lower() == 'rock') or 
          (user_play.lower() == 'scissors' and pc_play.lower() == 'paper')):
        print('You have won, congratulations!')
    return

def main():
    while True:
        game()
        play_again = input('Play again? [Y/N]: ') == 'Y'
        if not play_again:
            print('Thanks for playing, have a good day!')
            return
main()