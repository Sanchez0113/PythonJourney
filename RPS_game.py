import random
import math

def play():
    user = input("What's your choice? 'r' for rock, 'p' for paper, 's' for sissors\n")
    user = user.lower()

    computer = random.choice(['r','p','s'])

    if user == computer:
        return (0, user, computer)
    
    if is_win(user, computer):
        return (1, user, computer)
    
    return (-1, user, computer)

def is_win(player, opponent):
    if (player == 'r' and opponent == 's') or (player == 's' and opponent == 'p') or (player == 'p' and opponent == 'r'):
        return True
    return False


def play_best_of(n):
    player_wins = 0
    computer_wins = 0
    wins_necessary = math.ceil(n/2)
    while player_wins < wins_necessary or computer_wins < wins_necessary:
        result, user, computer = play()

        if result == 0:
            print("It is a tie. You and the computer have both chosen {}. \n".format(user))
        elif result == 1:
            print("You have chosen {} and the computer has chosen {}. You won! \n".format(user,computer))
        else:
            print("You have chosen {} and the computer has chosen {}. You lost. \n".format(user,computer))
        print('\n')

    if player_wins > wins_necessary:
        print('You have won {} times. Congratz! \n'.format())
    else:
        print('The computer has won {} time. You lose, better luck next time. \n'.format(n) )



if __name__ == '__main__':
    play_best_of(3)