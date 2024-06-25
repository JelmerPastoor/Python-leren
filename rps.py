import numpy as np
print('Welcome to Rock Paper Scissors!')
def user():
    user_play = input('Please enter rock, paper, or scissors!')
    return user_play

# Rules: Rock beats scissors, scissors beats paper, paper beats rock
def computer():
    pc_choices = ['rock', 'paper', 'scissors']
    pc_play = np.random.choice(pc_choices)
    return pc_play

user()
computer()
