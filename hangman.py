"""
File: hangman.py
-----------------------------
This program plays hangman game.
Users sees a dashed word, trying to
correctly figure the un-dashed word out
by inputting one character each round.
If the user input is correct, show the
updated word on console. Players have N_TURNS
to try in order to win this game.
"""


import random


# This constant controls the number of guess the player has
N_TURNS = 7


def main():
    """
    TODO:
    have a random word to be guessed
    input character and have a guessing result
    end by winning the game (guess the complete word)
    or by using up the turns (7 times)
    """
    word = random_word()  # the word user is going to guess in the game
    guess = ""  # have a empty initial string
    for i in range(len(word)):
        guess += "-"

    print("The word looks like: ", end="")
    print(guess)

    n = N_TURNS

    while True:  # infinite loop, end by the winning and losing situation
        if guess.isalpha() == True:  # where the game ends in the winning situation
            print("you win!")        # If the "-" are all replaced by alphabet, user wins
            print('The word was: ' + str(word))
            break
        else:
            g = input_process().upper()  # case insensitive
            if word.find(g) != -1:  # when the ch entered by user is a correct guess
                for i in range(len(word)):    # test every characters in the word string and:
                    if g == word[i]:          # replace every "-" in the guess string by the ch entered by user
                        guess = guess[:i] + g + guess[i+1:]  # re-make the string
                print('You are correct!')
                print('The word looks like: ' + str(guess))
                print('You have ' + str(n) + " times left")

            else:
                n -= 1  # if the guess is not good, count the remaining turns
                if n == 0:  # when run out of turns, end game in the losing situation
                    print("You are completely hung :(")
                    print('The word was: ' + str(word))
                    break
                else:  # still have remaining turns and print the current situation for user
                    print('There is no ' + str(g) + "'s in the word")
                    print("The word looks like: ", end="")
                    print(guess)
                    print("you have " + str(n) + " times left")





def input_process():
    while True:
        l = ""
        l = input('Your Guess: ')
        if l.isalpha() == False:  # if input is not a "single character", let the user input again
            print("Illegal format.")
        elif len(l) > 1:
            print("Illegal format.")
        else:
            return l




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
