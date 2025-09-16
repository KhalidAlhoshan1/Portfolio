Number guessing game

This is a Python game between the user and the Computer, the Computer randomly generates a number and the user must guess the number correctly.

How it works
- The program tries to open a High Score JSON file to check the user's previous tries and check the user's high score, if the file doesn't exist the program makes a new one
- If the high score file already exists, the user is given a message that says the previous high score and encourages the player to try and beat it
- The user is prompted to guess between 1 and 15, if the guess is too low they are notified by a message, if the guess is too high the same happens, this keeps going on untill the user guesses correctly or types 'q' to exit
- if the user enters any value outside of the range of 1-15 they're prompted with a message that tells them to stick with the range given and enter a correct value or enter 'q' to exit
- After the user guesses the correct number the program checks if the user got a new high score and saves it in the JSON file, then the user is prompted to play again or quit the game

variable filename on line 5 must have a correct path before running the program so that the program can create/read JSON file for high score
