######################################################################
# Author: Dr. Scott Heggen      TODO: Change this to your names
# Username: heggens             TODO: Change this to your usernames
#
# Assignment: T6: Funky Functions
# Purpose:  Some functions to play around with and understand return values
#           This function sings you the willaby wallaby children's song
#
######################################################################
# Acknowledgements:
#   Original Author: Dr. Scott Heggen
#
#   Inspired by Raffi: https://www.youtube.com/watch?v=sOOZQZlxxC4
#
# licensed under a Creative Commons
# Attribution-Noncommercial-Share Alike 3.0 United States License.
####################################################################################


def willoughby_wallaby(name):
    """
    A function that converts the first letter(s) of your name to a "W"

    :param name: Your name
    :return: Your name, with the first one or two letters replaced with a "W"
    """

    # A list of all the likely consonant blends
    consonant_blends = ["bl", "br", "ch", "ck", "cl", "cr",
                        "dr", "fl", "fr", "gh", "gl", "gr",
                        "ng", "ph", "pl", "pr", "qu", "sc",
                        "sh", "sk", "sl", "sm", "sn", "sp",
                        "st", "sw", "th", "tr", "tw", "wh", "wr"]

    if name[0:2].lower() in consonant_blends:   # if the first two letters are in the list above
        new_name = "W" + name[2:]               # Replace the first two letters
    else:
        new_name = "W" + name[1:]               # Else just replace the first letter
    return new_name                             # Return the modified name


def main():
    """
    A fun little program that sings the Willoughby Wallaby children's song.

    :return: None
    """

    your_name = ""
    while your_name != "STOP":
        your_name = input("What's your name (Enter STOP to stop the program)?\n")
        if your_name == "STOP":
            break
        w_name = willoughby_wallaby(your_name)
        print("Willaby, Wallaby " + w_name)
        print("An elephant sat on " + your_name + "!")

if __name__ == "__main__":
    main()
