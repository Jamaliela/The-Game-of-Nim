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
    This function asks the user to input the number of balls in order to start the game
    :return:
    """

    num_balls = int(input("how many balls do you want to start with?"))                     # asks the user to enter number of balls
    while num_balls < 15:                                                                   # while function to check if the input is less than 15
        num_balls = int(input("Please enter a number equal or greater than 15"))            # make the user enter the number of balls again
    print("you are starting with", num_balls, "balls")
    return num_balls


def player_1_turn(num_balls):
    """

    :return:
    """

    player1 = int(input("How many balls do you wanna take? Please choose from 1 to 4:"))
    while (player1 < 1) and (player1 > 4):
        player1 = int(input("Not an option, try again"))
    num_balls = num_balls - player1
    print("you took", player1, "balls")
    print("there are", num_balls, "left")
    return num_balls


def player_2_turn(num_balls):

    player2 = num_balls % 5
    if player2 == 0:
        player2 = 1
    num_balls = num_balls - player2
    print("The computer takes", player2, "balls")
    print("there are", num_balls, "left")
    return num_balls


def main():
    """

    """

    turn = 0
    num_balls = getting_started()
    while num_balls > 0:
        num_balls = player_1_turn(num_balls)
        turn = 1
        if num_balls == 0:
            break
        num_balls = player_2_turn(num_balls)
        turn = 0
    if turn == "0":
        print("the computer wins")
    else:
        print("You win")


if __name__ == "__main__":

    main()
