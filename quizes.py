import random
words = [ 'win', 'mom','dad', 'car', 'tubsci' , 'wmdct' ,  'banana' , 'queue' , 'orange','giza','ztont']

correct_word = words[int(random.random() * len(words))]

hint_letter = correct_word[int(random.random() * len(correct_word))]

guess = input (f'Guess a word. Options are: {words}, hint : {hint_letter} > ')

color0 = '\033[0m'
red    = '\033[30;41m'
green  = '\033[33;42m'

if guess == correct_word:
    print(f'{green}enzo WINS 10 euro!!!{color0}')
else:
    print(f'{red}Losser!!!{color0}. The correct word was {correct_word}')









