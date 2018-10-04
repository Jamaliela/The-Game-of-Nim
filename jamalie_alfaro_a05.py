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
# Giorgi and Aaron (Lab - Tuesday night)
#
###############################################################################

import random                   # importing the random library

def getting_started():
    """
    This function asks the user to input the number of balls in order to start the game
    :return: None. void
    """

    num_balls = int(input("how many balls do you want to start with?"))                     # asks the user to enter number of balls
    while num_balls < 15:                                                                   # while function to check if the input is less than 15
        num_balls = int(input("Please enter a number equal or greater than 15"))            # make the user enter the number of balls again
    print("you are starting with", num_balls, "balls")                                      # telling the user the number of balls chosen for the game
    return num_balls


def player_1_turn(num_balls):
    """
    This function asks the user to choose how many balls to take and subtracts that number from the total number of balls.
    :param num_balls: integer. number of balls that changes as user and computer pick
    :return: updated number of balls.
    """

    player1 = int(input("How many balls do you wanna take? Please choose from 1 to 4:"))              # ask user to choose how many balls to take from 1 to 4
    list = (1,2,3,4)                                                                           # list of possible ball choices to pick
    while player1 not in list:                                                     # while loop to prevent user from choosing something else
        player1 = int(input("Not an option, try again"))                           # print statement to tell them to input another number of balls
    num_balls = num_balls - player1                                                # subtraction of user's pick from total number of balls
    print("you took", player1, "balls")                                            # telling user how many balls they pick
    print("there are", num_balls, "left")                                          # telling user how many balls are remaining
    return num_balls


def player_2_turn(num_balls):
    """
    This function divides the number of balls remaining by 5 with modulus so that the computer ends up winning by always taking the remainder of the division.
    :param num_balls: integer. number of balls that changes as user and computer pick
    :return: num_balls
    """

    player2 = num_balls % 5                             # modulus to calcuate how many balls for the computer to pick
    if player2 == 0:                                    # if the result from modulus is 0 then something else happens
        player2 = random.randrange(1, 4)                # a random number is assigned to player2
    num_balls = num_balls - player2                     # recalculating the number of balls after the computer picks
    print("The computer takes", player2, "balls")       # telling user how many balls they pick
    print("there are", num_balls, "left")               # telling user how many balls are remaining
    return num_balls


def main():
    """
    Function where we call the previous functions and also determine the winner.
    """

    turn = 0                                    # defining variable to compute who wins
    num_balls = getting_started()               # calling the getting started function
    while num_balls > 0:                        # while loop for when there are balls available (this will run both functions until there are no more balls)
        num_balls = player_1_turn(num_balls)    # the user's turn is run
        turn = 1                                # assigning turn = 1 to the user
        if num_balls == 0:                      # if the number of balls is zero then the loop will break
            break
        num_balls = player_2_turn(num_balls)     # the computer's loop is run
        turn = 0                                # assigning turn = 1 to the user
    if turn == 0:                                   # if function to compute who wins. if turn = 0 (player2 function is the last one to pick balls) then the computer wins.
        print("the computer wins")
    else:
        print("You win")                            # if turn = 1 (player1 function is the last one to pick balls) then the user wins.


if __name__ == "__main__":

    main()
