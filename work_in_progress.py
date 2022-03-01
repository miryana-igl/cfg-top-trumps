# The modules used in our code
import random
import requests
import re


player = input('Hello. Please enter in your name: ')

print()

# We started by introducing the Random Pokemon function which picks a random number and pulls the corresponding Pokemon
# off of the PokeAPI, pulling only the Name, ID, Height and Weight stats of the Pokemon.

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
# We added a game of chance as a fun way to begin our top trumps game.
# You and the opponent roll dice to find out who will go first.
# Whoever wins, gets to see their Pokemon stats and decides which stat they want to use.

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


    print('Opponent rolled', opponent)

    print()

    if your_choice > opponent:
        print('You go first.')
        print()
        my_run()
    elif your_choice is opponent:
        print('Tie! Roll again!')
        print()
        roll_die()
    else:
        print('{} loses. Opponent goes first.'.format(player))
        print()
        opponent_run()

print()

# One of the challenges was figuring out how to make the opponent run first if they've won the dice game
# The hardest bit was figuring out how to randomise their stat pick.
# Initially we thought about assigning a boolean value to the individual stat metrics, however this proved to be tricky
# so we ended up listing them under stat_list and pulling a random list item. A problem with this is that we don't get
# the stat string attached to the value, so we only know about the number assigned to that stat.

def opponent_run():

    print()

    opponent_pokemon = random_pokemon()
    print('The opponent chose {}'.format(opponent_pokemon['name']))
    print('{n}''s stats are: \nID number: {i} \nHeight: {h} \nWeight: {w}'.format(n=opponent_pokemon['name'],
                                                                                  i=opponent_pokemon['id'],
                                                                                  h=opponent_pokemon['height'],
                                                                                  w=opponent_pokemon['weight']))

    stats_list = ['id', 'height', 'weight']
    stat_choice = random.choice(stats_list)

    print()

    print("Opponent picked the following stat: {} ".format(opponent_pokemon[stat_choice]))
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
        print('ITS A DRAW! Re-Match!')
        roll_die()
    while True:
        roll_again = input('would you like to play again? (y/n)')
        if re.match('y', roll_again):
            roll_die()
        else:
            print("Thanks for playing!".format(input = roll_die))
            break

print()

# My_run is the function that is executed if the player wins the dice roll.
# You get to see your Pokemon stats, which gives you the advantage of choosing a good stat to fight with.

def my_run():
    my_pokemon = random_pokemon()
    print('You were given {}'.format(my_pokemon['name']))
    print('The {n} stats are: \nID number: {i} \nHeight: {h} \nWeight: {w}'.format(n=my_pokemon['name'], i=my_pokemon['id'], h=my_pokemon['height'], w=my_pokemon['weight']))

    print()

    my_stat_choice = input('Which stat do you want to use? (id, height, weight) ')

    print()

    opponent_pokemon = random_pokemon()
    print('The opponent chose {}'.format(opponent_pokemon['name']))
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
        print('ITS A DRAW! Re-Match!')

    while True:
        roll_again = input('would you like to play again? (y/n)')
        if re.match('y', roll_again):
            roll_die()
        else:
            print("Thanks for playing!".format(input = roll_die))
            break



roll_die()
