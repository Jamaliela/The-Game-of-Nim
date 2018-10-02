######################################################################
# Author: Emely Alfaro Zavala & Elaheh Jamali
# Username: Alfarozavalae & Jamalie
#
# Assignment: A05: The Game of Nim
#
# Purpose: Practice breaking a larger problem down into smaller "mental chunks" using functions
# Gain practice using loops and modulus (%)
#
######################################################################
# Acknowledgements:
#
#
###############################################################################


def getting_started():
    """

    :return:
    """

    global num_balls
    global limit
    num_balls = int(input("how many balls do you want to start with?"))
    limit = 15
    while num_balls < limit:
        print("Please enter a number equal or greater than 15")
    print("you are starting with", num_balls, "balls")
    return num_balls


def player_1_turn():
    """

    :return:
    """

    global player1
    global num_balls
    global turn
    player1 = int(input("How many balls do you wanna take? Please choose from 1 to 4:"))
    limit1 = 4
    turn = 1
    while player1 > limit1:
        print("Not an option, try again")
    num_balls = num_balls - player1
    print("you took", player1, "balls")
    print("there are", num_balls, "left")
    return num_balls, turn


def player_2_turn():
    global num_balls
    global turn
    turn = 0
    player2 = num_balls % 5
    if player2 == 0:
        player2 = 1
    num_balls = num_balls - player2
    print("The computer takes", player2, "balls")
    print("there are", num_balls, "left")
    return num_balls, turn


def main():
    """

    """


getting_started()

limit = 1
while num_balls > limit:
    player_1_turn()
    player_2_turn()
if turn == "0":
    print("the computer wins")
else:
    print("You win")


main()
