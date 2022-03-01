
import random
import requests
import re

# This bit of the code rolls a die and tells you if you go first
player = input('Hello. Please enter in your name: ')

print()

def random_pokemon():
    pokemon_number = random.randint(1, 151)
    url = 'https://pokeapi.co/api/v2/pokemon/{}/'.format(pokemon_number)
    response = requests.get(url)
    pokemon = response.json()
    return {
        'name': pokemon['name'],
        'id': pokemon['id'],
        'height': pokemon['height'],
        'weight': pokemon['weight'],
    }

def roll_die():
    your_choice = random.randint(1, 6)

    print()

    opponent = random.randint(1, 6)

    while True:
        your_roll = input('Feeling lucky? Type roll to roll the die ')

        if not re.match('roll', your_roll):
            print("Error, please type roll".format(input=your_roll))
            continue
        else:
            # correct input given! we can continue!
            break

    print()

    print('You rolled', your_choice)

    print()


    print('Your opponent rolled', opponent)

    print()

    if your_choice > opponent:
        print('You go first.')
        print()
        my_run()
    elif your_choice is opponent:
        print('Its a tie! Please Roll again!')
        print()
        roll_die()
    else:
        print('{} loses. Your opponent goes first.'.format(player))
        print()
        opponent_run()

print()


def opponent_run():

    print()

    opponent_pokemon = random_pokemon()
    print('Your opponent chose {}'.format(opponent_pokemon['name']))
    print('{n}''s stats are: \nID number: {i} \nHeight: {h} \nWeight: {w}'.format(n=opponent_pokemon['name'],
                                                                                  i=opponent_pokemon['id'],
                                                                                  h=opponent_pokemon['height'],
                                                                                  w=opponent_pokemon['weight']))

    stats_list = ['id', 'height', 'weight']
    stat_choice = random.choice(stats_list)

    print()

    print("Your opponent picked the following stat: {} ".format(opponent_pokemon[stat_choice]))
    opponent_stat_choice = opponent_pokemon[stat_choice]

    print()

    my_pokemon = random_pokemon()
    print('You were given {}'.format(my_pokemon['name']))

    print('The {n} stats are: \nID number: {i} \nHeight: {h} \nWeight: {w}'.format(n=my_pokemon['name'],
                                                                                   i=my_pokemon['id'],
                                                                                   h=my_pokemon['height'],
                                                                                   w=my_pokemon['weight']))
    my_stat = my_pokemon[stat_choice]

    print()

    if my_stat > opponent_stat_choice:
        print('{} WINS!'.format(player))
    elif my_stat < opponent_stat_choice:
        print('{} LOSES!'.format(player))
    else:
        print('ITS A DRAW! ')

print()

def my_run():
    my_pokemon = random_pokemon()
    print('You were given {}'.format(my_pokemon['name']))
    print('The {n} stats are: \nID number: {i} \nHeight: {h} \nWeight: {w}'.format(n=my_pokemon['name'], i=my_pokemon['id'], h=my_pokemon['height'], w=my_pokemon['weight']))

    print()

    my_stat_choice = input('Which stat do you want to use? (id, height, weight) ')

    print()

    opponent_pokemon = random_pokemon()
    print('Your opponent chose {}'.format(opponent_pokemon['name']))
    print('{n}''s stats are: \nID number: {i} \nHeight: {h} \nWeight: {w}'.format(n=opponent_pokemon['name'],
                                                                                  i=opponent_pokemon['id'],
                                                                                  h=opponent_pokemon['height'],
                                                                                  w=opponent_pokemon['weight']))
    my_stat = my_pokemon[my_stat_choice]
    opponent_stat = opponent_pokemon[my_stat_choice]

    print()

    if my_stat > opponent_stat:
        print('{} WINS!'.format(player))
    elif my_stat < opponent_stat:
        print('{} LOSES!'.format(player))
    else:
        print('ITS A DRAW!')

    while True:
        roll_again = input('would you like to play again? (y/n)')
        if re.match('y', roll_again):
            roll_die()
        else:
            print("Thanks for playing!".format(input = roll_die))
            break


roll_die()