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
####################################################################################


def getting_started():
    """
    Boolean function takes an integer as input. Returns True if even and False if odd


    """

    global num_balls
    num_balls = int(input("how many balls do you want to start with?"))
    limit = 15
    while num_balls < limit:
        print("Please enter a number equal or greater than 15")
    print("you are starting with", num_balls, "balls")


def player_1_turn():
    global player1
    player1 =int(input("How many balls do you wanna take? Please choose from 1 to 4:"))
    limit1 = 4
    while player1 > limit1:
        print("Not an option, try again")
    return print("you took", player1, "balls")


def player_2_turn():
    global player2
    player2 = num_balls - player1
    player2 = player2 % 5
    return print("The computer takes", player2, "balls")


def main():
    """

    """


getting_started()

limit = 0
while num_balls > limit:
    player_1_turn()
    player_2_turn()
    num_balls = num_balls - player2

print("Game over")

main()
