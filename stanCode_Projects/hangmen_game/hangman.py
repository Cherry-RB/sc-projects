"""
File: hangman.py
Name:Cherry
-----------------------------
This program plays hangman game.
Users sees a dashed word, trying to
correctly figure the un-dashed word out
by inputting one character each round.
If the user input is correct, show the
updated word on console. Players have N_TURNS
chances to try and win this game.
"""


import random


# This constant controls the number of guess the player has.
N_TURNS = 7


def main():
    """
    TODO:
    Let player guess the right answer.
    If the player guess right alphabet,we need to renew the reminder and the times of guesses left.
    """
    answer = random_word()  # set the answer
    # give player the reminder:use dash to cover every word of answer
    dashed = ''
    for i in range(len(answer)):
        dashed += '-'
    # let player to play
    input_ch(N_TURNS, answer, dashed)
    print('You win!!')
    print('The word was:'+str(answer))


def input_ch(N_TURNS, answer, dashed):
    while dashed.find('-') != -1:  # let player play until finding the right answer
        print('The word looks like:' + dashed)
        print('You have ' + str(N_TURNS) + ' guesses left.')
        guess = input('Your guess: ')
        while not guess.isalpha() or not len(guess) == 1:  # make sure the player input one alphabet
            print('illegal format.')
            guess = input('Your guess: ')
        guess = guess.upper()
        if answer.find(guess) != -1:  # if player guess right alphabet(當guess有在answer出現)
            # renew the reminder
            new_dashed = ''  # make new string(給個新竹籤)
            # according the length of answer to decide how many words in the string(依照答案長度，逐個插字母)
            for i in range(len(answer)):
                if answer[i] == guess:  # renew part(把這次猜對的插進去)
                    new_dashed += guess
                else:  # keep part(把其他的原樣插上去)
                    ch = dashed[i]
                    new_dashed += ch
            dashed = new_dashed  # (更新現有的答案)
            print('You are correct!')
        else:
            print('There is no '+str(guess)+'\'s in the word.')
            N_TURNS -= 1
    return


def random_word():
    num = random.choice(range(9))
    if num == 0:
        return "NOTORIOUS"
    elif num == 1:
        return "GLAMOROUS"
    elif num == 2:
        return "CAUTIOUS"
    elif num == 3:
        return "DEMOCRACY"
    elif num == 4:
        return "BOYCOTT"
    elif num == 5:
        return "ENTHUSIASTIC"
    elif num == 6:
        return "HOSPITALITY"
    elif num == 7:
        return "BUNDLE"
    elif num == 8:
        return "REFUND"


#####  DO NOT EDIT THE CODE BELOW THIS LINE  #####
if __name__ == '__main__':
    main()
