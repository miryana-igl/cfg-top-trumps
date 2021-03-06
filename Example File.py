
import random
import requests
import re

#This bit of the code rolls a die and tells you if you go first

def roll_die():
    player = input('Player name: ')

    your_choice = random.randint(1,2)
    opponent = random.randint(1,2)

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
    elif your_choice is opponent:
        print('Tie! Roll again!')




    else:
        print('{} loses. Opponent goes first.'.format(player))


#This bit of the code gets a random number and assigns the Pokemon to the player and the opponent

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

def run ():
    my_pokemon = random_pokemon()
    print('You were given {}'.format(my_pokemon['name']))
    print('The {n} stats are: \nID number: {i} \nHeight: {h} \nWeight: {w}'.format(n = my_pokemon['name'], i = my_pokemon['id'], h = my_pokemon['height'], w = my_pokemon['weight']))

    stat_choice = input('Which stat do you want to use? (id, height, weight) ')
    opponent_pokemon = random_pokemon()
    print('The opponent chose {}'.format(opponent_pokemon['name']))
    print('{n}''s stats are: \nID number: {i} \nHeight: {h} \nWeight: {w}'.format(n = opponent_pokemon['name'], i = opponent_pokemon['id'], h = opponent_pokemon['height'], w = opponent_pokemon['weight']))
    my_stat = my_pokemon[stat_choice]
    opponent_stat = opponent_pokemon[stat_choice]
    if my_stat > opponent_stat:
        print('You Win!')
    elif my_stat < opponent_stat:
        print('You Lose!')
    else:
        print('Draw!')


roll_die()
run()