print('''*****Commands*****
S - Scissors
R - Rock
P - Paper
Quit - to Quit
Help - to Show Commands
Score - to Show Points\n''')   # Commands
Quit = False        # Quit Boolean
player1 = ""        # Initialization
player2 = ""        # Initialization
P1points = 0        # Player 1 Points
P2points = 0        # Player 2 Points
MaxPoints = 3       # Max Points
detail = {          # Dictionary
    "R": "Rock",
    "S": "Scissors",
    "P": "Paper"
}

while P1points < MaxPoints and P2points < MaxPoints:    # Loop until Max Points
    while player1.upper() != "R" and player1.upper() != "S" and player1.upper() != "P":    # Filter of Commands
        player1 = input("Player 1: ").upper()       # Uppercase all input
        if player1 == "HELP":       # Show Commands
            print('''*****Commands*****
S - Scissors
R - Rock
P - Paper
Quit - to Quit
Help - to Show Commands
Score - to Show Points\n''')        # Long Line

        elif player1 == "QUIT":
            Quit = True
            break       # Quit from current Loop
        elif player1 == "SCORE":       # Show points (Change it to function)
            print(f'*****Score*****\nPlayer 1: {P1points} \nPlayer 2: {P2points}\n')
    if not Quit:
        while player2.upper() != "R" and player2.upper() != "S" and player2.upper() != "P":     # Filter of Commands
            player2 = input("Player 2: ").upper()       # Uppercase all input
            if player2 == "HELP":       # Show Commands
                print('''\n*****Commands*****
S - Scissors
R - Rock
P - Paper
Quit - to Quit
Help - to Show Commands
Score - to Show Points\n''')       # Long Line

            elif player2 == "QUIT":
                Quit = True
                break       # Quit from current Loop
            elif player2 == "SCORE":       # Show points (Change it to function)
                print(f'*****Score***** \nPlayer 1: {P1points} \nPlayer 2: {P2points}\n')

    # Rock, Paper, and Scissors' Logic
    if player1 == player2:
        msg = "Draw!"

    elif player1 == "P":
        if player2 == "S":
            msg = "You Lose!"
        else:
            msg = "You Win!"

    elif player1 == "S":
        if player2 == "R":
            msg = "You Lose!"
        else:
            msg = "You Win!"

    else:
        if player2 == "P":
            msg = "You Lose!"
        else:
            msg = "You Win!"
    # Until Here

    if not Quit:    # Show Result if not Quit
        print(f'\nPlayer 1: {detail.get(player1)} \nPlayer 2: {detail.get(player2)} \n{msg}\n')
        player2 = ""
        player1 = ""
        if msg == "You Win!":
            P1points += 1
            winner = "Player 1"
        elif msg == "You Lose!":
            P2points += 1
            winner = "Player 2"
        print(f'*****Score*****\nPlayer 1: {P1points} \nPlayer 2: {P2points}\n')

    else:           # Quit || End Process
        break       # Exit From the Outer Loop
print(f'The winner of this Epic Jack n Poy is {winner}!')       # Prints the Winning Player