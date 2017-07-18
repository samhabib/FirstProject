''' Generate a random number between 1 and 9 (including 1 and 9). Ask the user to guess the number, then tell them
whether they guessed too low, too high, or exactly right. (Hint: remember to use the user input lessons from the very
first exercise)

Extras:

    Keep the game going until the user types “exit”
    Keep track of how many guesses the user has taken, and when the game ends, print this out.
'''

import random

guesses = 0
correct = 0

Loop = True
while Loop:
    a = random.randint(1, 9)
    check = input("Guess a number between 1 and 9 ")
    if check == a:
        print("Correct! The number was %s" % a)
        guesses += 1
        correct += 1
    else:
        print("Incorrect! The number was %s" % a)
        guesses += 1

    exit = input("If you want to stop the program type in 'exit' else press enter to continue ")
    if exit == 'exit':
        Loop = False

print("You had %s guesses and were correct %s times" % (guesses, correct))
