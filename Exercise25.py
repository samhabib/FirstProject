'''In a previous exercise, we’ve written a program that “knows” a number and asks a user to guess it.

This time, we’re going to do exactly the opposite. You, the user, will have in your head a number between 0 and 100.
The program will guess a number, and you, the user, will say whether it is too high, too low, or your number.

At the end of this exchange, your program should print out how many guesses it took to get your number.

As the writer of this program, you will have to choose how your program will strategically guess. A naive strategy can
 be to simply start the guessing at 1, and keep going (2, 3, 4, etc.) until you hit the number. But that’s not an
 optimal guessing strategy. An alternate strategy might be to guess 50 (right in the middle of the range), and then
 increase / decrease by 1 as needed. After you’ve written the program, try to find the optimal strategy! 
 '''


print("Think of a number for the computer to guess between 0 and 100")

a = True
count = 0
floor = -1
ceiling = 100

while a:
    computerGuess = (ceiling + floor) // 2
    print(computerGuess)
    count += 1
    userInput = input("Is the computer's guess too high 'hi', too low 'lo' , or 'correct'?: ")
    userInput = str(userInput)

    if userInput == 'hi':
        ceiling = computerGuess + 1

    elif userInput == 'lo':
        floor = computerGuess + 1

    elif userInput == 'correct':
        print("Congratulations it took the computer %s guesses to correctly get your answer" % count)
        a = False

    else:
        print("You messed up so the computer will guess again")
