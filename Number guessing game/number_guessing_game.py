"""Computer generates random number, user tries to guess correctly, save user high score in json file"""
import random
import json

filename = 'C:/Users/kalho/OneDrive/Documents/Portfolio/Number guessing game/high_score.json'

#load High score in json file
try:
    with open(filename) as f:
        high_score = json.load(f)
except FileNotFoundError:
    high_score = None

print("\nThis is a number guessing game, you try to guess the correct number that the computer randomly generated, try to guess it correctly in the least number of tries.\n")

if high_score is not None:
    print(f"The current high score is {high_score} guesses, try to guess the number in less tries to score a new high score!")

while True:
    guess_counter = 0
    random_num=random.randint(1,15)
    
    while True:
        try:
            guess = input(f"\nGuess a number between 1 and 15, if you want to stop type 'q' :")
            
            if guess.lower() == 'q':
                print("Exiting the game...")
                exit()
            
            guess = int(guess)
            guess_counter+= 1

            if guess == random_num:
                print(f"\nCorrect! the number is {random_num} and you guessed it correctly in {guess_counter} tries!")
                break
            elif guess > random_num:
                print("Try lower")
            else:
                print("Try higher")
        except ValueError:
                print("Please enter a number between 1 and 15 or the letter 'q' to quit the game")

        
                
#high score check after correct guess
    if high_score is None or guess_counter < high_score:
        with open(filename, 'w')as f:
            json.dump(guess_counter,f)
        print(f"New high score! you set a new record with {guess_counter} guesses!")
        high_score = guess_counter
    else:
        print(f"You guessed correctly in {guess_counter} guesses!. The high score is {high_score} guesses, try to beat it!")

    play_again = input("\nDo you want to play again? (y/n): ").lower()
    if play_again !='y':
        print("\nThank you for playing my game!")
        break