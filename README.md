# A05: The Game of Nim

Name 1: Emely Alfaro

Name 2 (if needed): Elaheh Jamali

Repository Link: https://github.com/fall-2018-csc-226/a05-the-game-of-nim-ela-emely-a05.git

Google Document Link: https://docs.google.com/document/d/1QCkkTJ0cjxPQxYkkIRQLXBmJirHROU35bwyF4X8UGlA/edit?usp=sharing

---

This document is written in a language called Markdown, which is similar to HTML or other text-formatting languages. A helpful cheat sheet for Markdown is [here](https://github.com/adam-p/markdown-here/wiki/Markdown-Cheatsheet)

## INITIAL DESIGN PLAN:

Design a plan which meets the computational requirements to solve the problem. Your plan does not need to be syntactically correct. It needs to capture the flow of logic in a human readable format.

1. We will create the first function to ask the user for the number of balls but we will let them know that they have to choose a number >15
2. We will use aa while loop to print that they must enter another input if it is not equal or greater than 15.
3. we will print a string telling the user their number of balls.

1. our second function will be for the user's turn and we will start asking the user for an input
2. we will use a while function that checks that the input is not greater than four and that is not less than 1
3. we will subtract the input from the number of balls they picked in the first function

1. our third function will be for the computer's turn and the computer will take the number of balls and divide it by 5 using modulus.
2. we think we can make the computer pick the number of balls based on the modulus operation

1. in our main function we will call the functions and set a while loop to run until there is only one ball.
2. to determine the winner we wil assign variables to the turn functions and check in which one it ends. we will use if to check and print a sentence saying who won.


## IMPLEMENTATIONS:

A list in bullet form of each function you created, and what is each function’s purpose.

- getting_started: This function asks the user to input the number of balls in order to start the game.

- player_1_turn: This function asks the user to choose how many balls to take and subtracts that number from the total number of balls.

- player_2_turn: This function divides the number of balls remaining by 5 with modulus so that the computer ends up winning by always taking the remainder.

main: Function where we call the previous functions and also determine the winner.



## TESTING:

We are not sure of which functions we will end up testing but after asking in the lab we know that only fruitful functions can be tested. we can not test the user's inputs because
we can not know for sure what their pick would be.
we will do testing for the computer's turn and we expect to be able to test different number of balls with modulus and return the computer's pick (a number between 1 and 4 that is the remainder of the division)


## ERRORS:

- entering number of balls: our function would keep on looping because we had defined a limited variable instead of using the number directly
- updating number of balls: whenever it was the computer's turn, our coding kept on subtracting the computer's pick from the user's input. (the computer would not subtract the user's pick and then update the number of balls)
- subtracting balls at the end: the loop would run but it would subtract more balls at the end and return a negative number.
- definning global variables: this was probably our biggest problem because we tried making the number of balls global but it would not work. we had to user paramenters instead.


## SUMMARY:

We started trying to figure out how we wanted our code to look in a classroom in draper. We used a board to write the first function to take the input
for number of balls but we did not know that the same variable was going to give us trouble later.
in the board we also planned the users's turn and the computer's turn. after putting it in the board, we would start typing an encounter errors. the usual errors
were semantic because we were forgettign something or mistyping. As Ela was writing on the board, she would come up with names for the
variables but I would want to change those. changing the variable's name would make me take longer to type because I would be modyfing it.
in all the functions we tried stablishing a limit instead of putting the number directly. Doing that gave us trouble because the function
would not detect issues but would not do what it was expected to do. (semantic error)

This assignment turned out to be harder than we expected it to be because we complicated ourselves way too much with the global variables
when there was an easier way that we were not trying because it would not work on our first attemp. our initial design change because
our thoughts developed more as we went coding and testing in the interpreter and by debugging our code.
the final result is good because we fixed the code, tested it and tried several possible scenarios. I like how we also made it possible
for the human to use the same remainder (modulus) logic to beat the machine.
we started this assignment on friday night primarily to prepare for class and ask questions but on monday night we worked on it from 7.30pm until
midnight and got it working but not so efficiently. on tuesday night we went to the lab for two hours and fixed the issues and on wednesday night
we finished the details, made sure everything was completed and tested some more.



## COMMENTS:

A paragraph or so of your own comments on and reactions to this assignment. Consider this like a reflection.

This assignment as we said before, turned out to be harder than we initially though it would be because we wanted to do it in a certain way
that was not working, because we though we had to stablish limits for the while loops by using variables and because we worked on it for
several hours straight one night to the point of getting frustrated. we reflect on the team work that we have developed because we are good friends
who are learning from each other, trying to understand, seek for help and create something that makes both of us satisfied.
We also believe that the TAs are of great help when it comes to helping us figure out more efficient ways to do things or to simply
clarify things when we have questions. the assignment was fun, we learned a lot from it and look forward to the next one.
