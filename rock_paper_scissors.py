from numpy import random

weapons = ['Rock', 'Fire', 'Scissors', 'Snake', 'Human', 'Tree', 'Wolf', 'Sponge', 'Paper', 'Air', 'Water',
           'Dragon', 'Devil', 'Lightning', 'Gun']


def list_to_string_without_brackets(list1):
    return str(list1).replace('[', '').replace(']', '').replace("'", '')


lower_half_of_weapons_int = []
upper_half_of_weapons_int = []
inverse_lower_half_of_weapons_int = []
inverse_upper_half_of_weapons_int = []
w_half = (len(weapons) + 1) / 2

for num in range(1, (len(weapons))):
    if num < w_half:
        lower_half_of_weapons_int.append(num)
    elif num >= w_half:
        upper_half_of_weapons_int.append(num)
    else:
        print('error. possible wrong number of items in list')

for num in lower_half_of_weapons_int:
    inverse_lower_half_of_weapons_int.append(num * -1)

for num in upper_half_of_weapons_int:
    inverse_upper_half_of_weapons_int.append(num * -1)


loosing_weapons_result_int = inverse_lower_half_of_weapons_int + upper_half_of_weapons_int
winning_weapons_result_int = inverse_upper_half_of_weapons_int + lower_half_of_weapons_int

print('''
Hello and welcome to my game!
at any point type help to see commands.
would you like to start the game?
''')

command = input('>').lower()

while command != 'quit':
    if command == 'help':
        print(f'''
To start, type "start", to quit, type "quit" and to recieve this message again, type "help".
Once the game has started, please type:
{list_to_string_without_brackets(weapons[0:-1])} or {weapons[-1]} to give your decision.
'''
              )
        command = input('>').lower()
    elif command in ['start', 'yes', 'play', 'ok']:
        print(f'''
{list_to_string_without_brackets(weapons[0:-1])} or {weapons[-1]}?
''')
        player_guess = input('>').title()
        if player_guess in weapons:
            computer_guess_int = (random.randint(0, len(weapons)))
            computer_guess = weapons[computer_guess_int]
            player_guess_int = weapons.index(player_guess)
            result = computer_guess_int - player_guess_int

            if result == 0:
                print(f'''
computer chose {computer_guess} you Draw

would you like to play again?
''')
                command = input('>').lower()
            elif result in loosing_weapons_result_int:
                print(f'''
computer chose {computer_guess} you loose!

would you like to play again?
''')
                command = input('>').lower()
            elif result in winning_weapons_result_int:
                print(f'''
computer chose {computer_guess} you win!

would you like to play again?
''')
                command = input('>').lower()
            else:
                print(f'error. computer chose {computer_guess}')
        elif player_guess == 'Help':
            print(
                f'''
To start, type "start", to quit, type "quit" and to recieve this message again, type "help".
Once the game has started, please type:
{list_to_string_without_brackets(weapons[0:-1])} or {weapons[-1]}.''')
            command = 'start'
        else:
            print('''
I do not understand...
''')
            command = 'start'

    elif command in ['quit', 'no', 'leave', 'exit']:
        command = 'quit'
    else:
        print('''
I do not understand...

Would you like to start again?
''')
        command = input('>').lower()
print('''
Thanks for playing, good bye.
''')
