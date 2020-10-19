#This bit of the code rolls a die and tells you if you go first,
# ideally if you lose, the opponent bit should run (opponent_turn) so far broken

import random
import re

player = input('Player name: ')
def roll_die():


    while True:
        your_roll = input('Type roll to roll a die ')
        if not re.match('roll', your_roll):
            print("Error, please type roll".format(input = your_roll))
        continue
    else:
            #correct input given! we can continue!
        break
    

your_choice = random.randint(1, 6)
opponent = random.randint(1,6)

print('You rolled', your_choice)
print('Opponent rolled', opponent)
if your_choice > opponent:
  print('You go first.')
else:
  print('{} loses. Opponent goes first.'.format(player))
roll_die()
