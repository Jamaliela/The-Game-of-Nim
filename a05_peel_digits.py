######################################################################
# Author: Emily Lovell & Scott Heggen      TODO: Change this to your names
# Username: lovelle & heggens             TODO: Change this to your usernames
#
# Assignment: A05: The Game of Nim
#
# Purpose: This program is designed to demonstrate the use of Python's string capabilities
# as a method for peeling digits from an integer
#
######################################################################
# Acknowledgements:
#   Original Author: Dr. Jan Pearce
#
# licensed under a Creative Commons
# Attribution-Noncommercial-Share Alike 3.0 United States License.
####################################################################################

import random


def peel_digits(num):
    """
    Given a positive integer num, peel_digits returns a list filled with the digits
    eg. given 1984, peel_digits returns the list [1, 9, 8, 4]
    :param num: an integer to peel into a list of digits
    :return: A list where each element of the list is a digit from num
    """
    str_num=str(num)                # convert to string to utilize Python's strong string features
    digit_list=[]                   # create empty list

    while len(str_num) > 0:         # Notice this is slightly different than last time you saw this function
        digit_list.append(int(str_num[0]))          #Puts each digits into list
        str_num = str_num[1:]
    return digit_list


def print_digits(digit_list): # takes a Python list as input
    """
    Given any Python list, this function prints each list element

    :param digit_list: a list where each element of the list is a digit from a larger number
    :return: None
    """
    for digit in digit_list:
        print(digit)


def main():
    """
    This main function is intended to display the capabilities of the peel_digits() and print_digit() functions

    :return: None
    """

    year = random.randint(0, 2018)
    print("\nYear = "+ str(year))
    year_list = peel_digits(year) # put list returned from function into year_list
    print("\nDigits")
    print_digits(year_list)


main()
