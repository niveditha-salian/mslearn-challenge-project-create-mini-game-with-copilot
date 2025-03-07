# write logic for a game where user chooses one of the elements (rock, paper, scissors) and the computer randomly chooses one of the elements and the winner is decided based on the rules of the game
# Rock beats scissors.
# Scissors beat paper.
# Paper beats rock.
# If both players choose the same element, the game is a tie.
# ask the user if they want to play again
# if yes, play the game again
# if no, exit the game
# if the user enters an invalid choice, ask the user to enter a valid choice
# if the user enters an invalid choice more than 3 times, exit the game
# write the logic in a function called play_game
# call the play_game function

def play_game():
    import random
    choices = ["rock", "paper", "scissors"]
    user_choice = input("Enter your choice (rock, paper, scissors): ")
    computer_choice = random.choice(choices)
    print("Computer's choice: ", computer_choice)
    if user_choice not in choices:
        print("Invalid choice. Please enter a valid choice.")
        return
    if user_choice == computer_choice:
        print("It's a tie!")
    elif user_choice == "rock":
        if computer_choice == "scissors":
            print("You win!")
        else:
            print("Computer wins!")
    elif user_choice == "paper":
        if computer_choice == "rock":
            print("You win!")
        else:
            print("Computer wins!")
    elif user_choice == "scissors":
        if computer_choice == "paper":
            print("You win!")
        else:
            print("Computer wins!")
    play_again = input("Do you want to play again? (yes/no): ")
    if play_again == "yes":
        play_game()
    elif play_again == "no":
        return
    else:
        print("Invalid choice. Please enter a valid choice.")
        play_game()

play_game()