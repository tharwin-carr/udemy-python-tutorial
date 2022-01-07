'''
Rock, Paper, Scissors

rock = 1
paper = 2
scissors = 3

1 beats 3
1 loses 2

2 beats 1
2 loses 3

3 beats 2
3 loses 1

Import Random to create a Rock, Paper, Scissors Game!
'''

import random

def rock_paper_scissors():
    player1 = random.randint(1, 3)
    player2 = random.randint(1, 3)

    print('ROCK PAPER SCISSORS SHOOT!')

    if player1 == 1:
        if player2 == 1:
            print('rock Draws rock')
        elif player2 == 2:
            print('rock LOSES paper')
        else:
            print('rock BEATS scissors')
    elif player1 == 2:
        if player2 == 1:
            print('paper BEATS rock')
        elif player2 == 2:
            print('paper DRAWS paper')
        else:
            print('paper LOSES to scissors')
    else:
        if player2 == 1:
            print('scissors LOSES to rock')
        elif player2 == 2:
            print('scissors BEATS paper')
        else:
            print('scissors DRAWS scissors')

rock_paper_scissors()