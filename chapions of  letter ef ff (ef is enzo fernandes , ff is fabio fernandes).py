import random
#chose a nuber
player1 = input('Name of player 1? > ')
player2 = input('Name of player 2? > ')

correct = chr(97 + int(random.random() * 26))

color0 = '\033[0m'
yellow = '\033[30;44m'
green = '\033[33;42m'


while True:
    guess = input(f'{green}{player1}{color0} guess a letter [a-z] > ')
    if guess == correct:
        print (f"{green}{player1}{color0} is the CHAMPION! {player2} is chicken dinner :P")
        exit(0)

    guess = input(f'{yellow}{player2}{color0} guess a letter [a-z] > ')
    if (guess) == (correct):
        print (f"{yellow}{player2}{color0} is the CHAMPION! {player1} is chicken dinner :P")
        exit(0)
