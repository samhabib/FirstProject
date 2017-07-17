''' Make a two-player Rock-Paper-Scissors game. (Hint: Ask for player plays (using input), compare them, print out a
message of congratulations to the winner, and ask if the players want to start a new game)

Remember the rules:

    Rock beats scissors
    Scissors beats paper
    Paper beats rock
'''

a = 1
rock = 'rock'
paper = 'paper'
scissors = 'scissors'

while a == 1:
    player1 = input("Player 1 pick rock, paper, or scissors: ")
    player1 = str(player1)
    if player1 not in (rock, paper, scissors):
        print("incorrect input please restart")
        break

    player2 = input("Player 2 pick rock, paper, or scissors: ")
    player2 = str(player2)
    if player2 not in (rock, paper, scissors):
        print("incorrect input please restart")
        break

    if player1 == rock:

        if player2 == rock:
            check = input("You both threw rock it is a draw, if you want a rematch type in AGAIN: ")
            if check != 'AGAIN':
                break

        elif player2 == paper:
            check = input("Player 2 wins! If you want a rematch type in AGAIN: ")
            if check != 'AGAIN':
                break

        elif player2 == scissors:
            check = input("Player 1 wins! If you want a rematch type in AGAIN: ")
            if check != 'AGAIN':
                break

    elif player1 == paper:

        if player2 == rock:
            check = input("Player 1 wins! If you want a rematch type in AGAIN: ")
            if check != 'AGAIN':
                break

        elif player2 == paper:
            check = input("You both threw paper it is a draw, if you want a rematch type in AGAIN: ")
            if check != 'AGAIN':
                break

        elif player2 == scissors:
            check = input("Player 2 wins! If you want a rematch type in AGAIN: ")
            if check != 'AGAIN':
                break

    elif player1 == scissors:

        if player2 == rock:
            check = input("Player 2 wins! If you want a rematch type in AGAIN: ")
            if check != 'AGAIN':
                break

        elif player2 == paper:
            check = input("Player 1 wins! If you want a rematch type in AGAIN: ")
            if check != 'AGAIN':
                break

        elif player2 == scissors:
            check = input("You both threw paper it is a draw, if you want a rematch type in AGAIN: ")
            if check != 'AGAIN':
                break
