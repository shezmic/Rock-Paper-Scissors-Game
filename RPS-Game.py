/**
 * @author [shezmic]
 * @desc [description]
 */


import random

def play_rps():
    choices = ['rock', 'paper', 'scissors']
    computer_choice = random.choice(choices)
    user_choice = input("Choose rock, paper, or scissors: ").lower()

    if user_choice not in choices:
        print("Invalid input. Please choose rock, paper, or scissors.")
        return play_rps()

    print(f"Computer chose {computer_choice}")

    if user_choice == computer_choice:
        print("It's a tie!")
    elif (user_choice == 'rock' and computer_choice == 'scissors'):
        print("You win! Rock smashes scissors.")
    elif (user_choice == 'paper' and computer_choice == 'rock'):
        print("You win! Paper covers rock.")
    elif (user_choice == 'scissors' and computer_choice == 'paper'):
        print("You win! Scissors cut paper.")
    else:
        if computer_choice == 'rock' and user_choice == 'scissors':
            print("You lose! Rock smashes scissors.")
        elif computer_choice == 'paper' and user_choice == 'rock':
            print("You lose! Paper covers rock.")
        elif computer_choice == 'scissors' and user_choice == 'paper':
            print("You lose! Scissors cut paper.")

    play_again = input("Play again? (y/n): ").lower()
    if play_again == 'y':
        play_rps()

play_rps()
