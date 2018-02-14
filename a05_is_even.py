######################################################################
# Author: Dr. Scott Heggen      TODO: Change this to your names
# Username: heggens             TODO: Change this to your usernames
#
# Assignment: A5: The Game of Nim
#
# Purpose: This program is designed to demonstrate the use of Boolean functions
# and the modulus (%) operator which gives the remainder following a division
#
######################################################################
# Acknowledgements:
#   Original Author: Dr. Jan Pearce
#
# licensed under a Creative Commons
# Attribution-Noncommercial-Share Alike 3.0 United States License.
####################################################################################

import random


def is_even(num):
    """
    Boolean function takes an integer as input. Returns True if even and False if odd

    :param num: An integer
    :return: Boolean representing if the number is even (True) or odd (False)
    """
    return int(num) % 2 == 0     # Notice this is different than the last time you saw this function



def main():
    """
    This main function is intended to display the capability of the is_even function

    :return: None
    """
    stop = False
    while not stop:
        year = random.randint(0, 2015)
        print("\nA random year is " + str(year) + ".")
        if is_even(year):
            print(str(year)+ " is even.")
        else:
            print(str(year)+ " is odd.")
        stop_input = input("Would you like to stop? [Y|N]")
        if stop_input == "Y":
            stop = not stop


main()
