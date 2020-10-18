import random



#def roll_die():
your_roll = input('Type roll to roll a die ')
your_choise = random.randint(1, 6)

print('You rolled a {}'.format(your_choise))


opponent = random.randint(1,6)
print('Your opponent rolled a {}'.format(opponent))
if your_choise > opponent:
    print('You go first')
else:
    print('Your opponent goes first')
