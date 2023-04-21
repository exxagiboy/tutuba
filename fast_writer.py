import random
import time
words = ['s', 'w', 't' , 'g', 'm','d','r','e']

correct_word = words[int(random.random() * len(words))]

color0 = '\033[0m'
red    = '\033[30;41m'
green  = '\033[33;42m'
blue  = '\033[33;43m'

input('Get ready...')
t0 = time.time()
answer = input (f'Type {correct_word} REALLY FAST!! > ')
t1 = time.time()

if answer == correct_word:
    print(f'{red}You took {t1 - t0} seconds to write. {color0}')
else:
    print(f'{blue}Losser!!!{color0}. The correct word was {correct_word}')









