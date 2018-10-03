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

import sys


def testing(did_pass):
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

    testing(player_2_turn(14) == 10)




def player_2_turn(num_balls):

    player2 = num_balls % 5
    if player2 == 0:
        player2 = 1
    num_balls = num_balls - player2
    print("The computer takes", player2, "balls")
    print("there are", num_balls, "left")
    return num_balls


