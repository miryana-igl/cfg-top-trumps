
import random
import requests
import re

#This bit of the code rolls a die and tells you if you go first
player = input('Player name: ')

def random_pokemon ():
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
    your_choice = random.randint(1,6)
    opponent = random.randint(1,6)

    while True:
        your_roll = input('Type roll to roll a die ')
        if not re.match('roll', your_roll):
            print("Error, please type roll".format(input = your_roll))
            continue
        else:
             #correct input given! we can continue!
            break

    print('You rolled', your_choice)
    print('Opponent rolled', opponent)
    if your_choice > opponent:
         print('You go first.')
         my_run()
    elif your_choice is opponent:
        print('Tie! Roll again!')
        roll_die()
    else:
        print('{} loses. Opponent goes first.'.format(player))
        opponent_run()

def opponent_run():
    opponent_pokemon = random_pokemon()
    print('The opponent chose {}'.format(opponent_pokemon['name']))
    print('{n}''s stats are: \nID number: {i} \nHeight: {h} \nWeight: {w}'.format(n=opponent_pokemon['name'],
                                                                               i=opponent_pokemon['id'],
                                                                               h=opponent_pokemon['height'],
                                                                                w=opponent_pokemon['weight']))

    stats_list = ['id', 'height', 'weight']
    stat_choice = random.choice(stats_list)
    print("Opponent picked the following stat: {} ".format(opponent_pokemon[stat_choice]))
    opponent_stat_choice= opponent_pokemon[stat_choice]

    my_pokemon = random_pokemon()
    print('You were given {}'.format(my_pokemon['name']))
    print('The {n} stats are: \nID number: {i} \nHeight: {h} \nWeight: {w}'.format(n=my_pokemon['name'],
                                                                                   i=my_pokemon['id'],
                                                                                   h=my_pokemon['height'],
                                                                                   w=my_pokemon['weight']))
    my_stat = my_pokemon[stat_choice]

    if my_stat > opponent_stat_choice:
        print('{} Wins!'.format(player))
    elif my_stat < opponent_stat_choice:
        print('{} Loses!'.format(player))
    else:
        print('Draw!')

def my_run ():
    my_pokemon = random_pokemon()
    print('You were given {}'.format(my_pokemon['name']))
    print('The {n} stats are: \nID number: {i} \nHeight: {h} \nWeight: {w}'.format(n = my_pokemon['name'], i = my_pokemon['id'], h = my_pokemon['height'], w = my_pokemon['weight']))

    my_stat_choice = input('Which stat do you want to use? (id, height, weight) ')

    opponent_pokemon = random_pokemon()
    print('The opponent chose {}'.format(opponent_pokemon['name']))
    print('{n}''s stats are: \nID number: {i} \nHeight: {h} \nWeight: {w}'.format(n=opponent_pokemon['name'],
                                                                                  i=opponent_pokemon['id'],
                                                                                  h=opponent_pokemon['height'],
                                                                                  w=opponent_pokemon['weight']))
    my_stat = my_pokemon[my_stat_choice]
    opponent_stat = opponent_pokemon[my_stat_choice]

    if my_stat > opponent_stat:
        print('{} Wins!'.format(player))
    elif my_stat < opponent_stat:
        print('{} Loses!'.format(player))
    else:
        print('Draw!')

roll_die()

