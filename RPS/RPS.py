# Rock is 1, Paper is 2, Scissors is 3, use int 

import random
print(f"Hello and welcome to Rock paper scissors! the game is simple, pick Rock, Paper, or Scissors and defeat the computer by guessing correctly!\n")
play_counter = 0
while True:
    play_counter+=1

    player_choice = input("Type 1 for Rock, 2 for Paper, and 3 for Scissors: ")
    player_choice = int(player_choice)

    while player_choice < 1 or player_choice > 3:
        player_choice = int(input("Pick 1, 2 , or 3 please"))

    if player_choice == 1:
        player_choice_name = 'Rock'
    elif player_choice == 2:
        player_choice_name = 'Paper'
    else:
        player_choice_name = 'Scissors'

    print(f"You chose {player_choice_name}, now it's time for the computer to choose: \n")

    computer_choice = random.randint(1,3)
    
    if computer_choice == 1:
        computer_choice_name = 'Rock'
    elif computer_choice == 2:
        computer_choice_name = 'Paper'
    else:
        computer_choice_name = 'Scissors'

    print(f"The computer chose {computer_choice_name}\n")


    if player_choice == computer_choice:
        result = "Draw"
    elif (player_choice == 1 and computer_choice == 3) or (player_choice == 3 and computer_choice == 1):
        result = "Rock"
    elif (player_choice == 1 and computer_choice == 2) or (player_choice == 2 and computer_choice == 1):
        result = "Paper"
    elif(player_choice == 3 and computer_choice == 2) or (player_choice == 2 and computer_choice == 3):
        result = "Scissors"

    if result == "Draw":
        print("It's a draw!")
    elif result == player_choice_name:
        print("You win!")
    else:
        print("You lose")

    print("Do you want to play again? (Y/N)")
    ans = input().lower()
    if ans == 'n':
        break

print(f"You played {play_counter} times!\n")
print("Thank you for playing!")

