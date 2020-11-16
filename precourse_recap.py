# this is a simple program that randomly chooses a number from 1 to 6, and
# has the user try to guess what it is.

import random


answer = random.randint(1,6)

print('Guess the result of a dice roll. That\'s any number between 1 and 6.')
player_answer = int(input('What is your guess?'))
if player_answer == answer:
    print('Congratulations, you got it right!')
if player_answer < answer:
    print('Sorry, your guess was too low.')
if player_answer > answer:
    print('Sadly, your guess was too high.')
