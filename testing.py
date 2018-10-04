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
###############################################################################
import random
import sys


def testit(did_pass):
    """
    Print the result of a unit test.

    This function works correctly--it is verbatim from the textbook, Chapter 6.

    You should reuse this function anytime you are creating a custom test suite

    :param did_pass: Boolean representing if the unit test passed or failed
    :return: None
    """

    linenum = sys._getframe(1).f_lineno         # Get the caller's line number.
    if did_pass:
        msg = "Test at line {0} ok.".format(linenum)
    else:
        msg = ("Test at line {0} FAILED.".format(linenum))
    print(msg)


def player2_testsuite():

    """
    The test suite function utilizes the testit() function,
    and is designed to test the player_2_turn() function,
    returning True only when the modulus division is correct.

    :return: None
    """
    print("\nRunning player_2_turn_testsuite()).")

    # working tests
    testit(player_2_turn(14) == 10)         # because 14 % 5 = 4 (there will be 10 balls remaining)
    testit(player_2_turn(17) == 15)         # because 17 % 5 = 2 (there will be 15 balls remaining)
    testit(player_2_turn(18) == 15)         # because 18 % 5 = 3 (there will be 15 balls remaining)
    testit(player_2_turn(23) == 20)         # because 23 % 5 = 3 (there will be 20 balls remaining)
    testit(player_2_turn(41) == 40)         # because 41 % 5 = 1 (there will be 40 balls remaining)
    testit(player_2_turn(34) == 30)         # because 34 % 5 = 4 (there will be 30 balls remaining)

    # TODO ADD MORE UNIT TESTS HERE!

    print("Run of player_2_turn_testsuite() complete.")

def player_2_turn(num_balls):
    """
    This function divides the number of balls remaining by 5 with modulus so that the computer ends up winning by always taking the remainder of the division.
    :param num_balls: integer. number of balls that changes as user and computer pick
    :return: None
    """

    player2 = num_balls % 5
    if player2 == 0:
        player2 = random.randrange(1, 4)
    num_balls = num_balls - player2
    # print("The computer takes", player2, "balls")
    # print("there are", num_balls, "left")
    return num_balls

def main():
    """
    Function to call the test suite.
    """
    player2_testsuite()


if __name__ == "__main__":

    main()
