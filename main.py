from constant import RULES, CHOICE_ELEMENT, scoreset
from random import choice
from decorators import log_time

number_of_set = int(input('please insert number of total set? : '))

# Number of matches per set
number_of_match = int(input('please insert number of total match in per set? : '))


def system_choice():
    return choice(RULES)


def user_choice():
    user = input("please insert your choice(r,p,s)?: ")
    if user not in RULES:
        print("OOOps!!!! your choice is incorect , please insert again?")
        return user_choice()
    return user


def find_winner(user_choice1, system_choice1):
    choices_system_user = {user_choice1, system_choice1}
    if len(choices_system_user) == 1:
        return None
    result = tuple(sorted(choices_system_user))
    return CHOICE_ELEMENT[result]


counter_of_set = 0


def calculate_set(scoreboard):
    global counter_of_set
    counter_of_set += 1
    if scoreboard['system'] == number_of_match:
        msg_set = f'You lose set {counter_of_set}'
        scoreset['system_set'] += 1
    else:
        msg_set = f'You win set {counter_of_set}'
        scoreset['user_set'] += 1

    print('#' * 50)
    print(msg_set)
    print(f'scoreset in match :   system - user : {scoreset["system_set"]} - {scoreset["user_set"]}')
    print('#' * 50)

    if counter_of_set < number_of_set:
        play_one_hand()

    elif scoreset['system_set'] == number_of_set:
        print('/' * 30)
        msg_end = f" end of finell " \
                  f"winner is system "
        print(msg_end)
        print('/' * 30)
    else:
        print('/' * 30)
        msg_end = f" end of finell " \
                  f"winner is user "
        print(msg_end)
        print('/' * 30)

def play_one_hand():
    scoreboard = {'user': 0, 'system': 0}
    while (scoreboard['user'] < number_of_match) and (scoreboard['system'] < number_of_match):
        user = user_choice()
        system = system_choice()
        winner = find_winner(user, system)

        if winner == user:
            scoreboard['user'] += 1
            msg = " You win"

        elif winner == system:
            scoreboard['system'] += 1
            msg = "You lose"

        else:
            msg = 'Draw'

        print('*' * 50)
        print(f'system choice: {system}  user choice : {user}  result : {msg}')
        print(f'scoreboard in match :   system - user : {scoreboard["system"]} - {scoreboard["user"]}')
        print('*' * 50)
    if scoreset['system_set'] < number_of_set and scoreset["user_set"] < number_of_set:
        calculate_set(scoreboard)


@log_time
def play():
    play_one_hand()


if __name__ == '__main__':
    play()
