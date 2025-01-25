import random

choice_list = ["rock", "paper", "scissors"]
computer_choice = random.choice(choice_list)

while True:
    player_choice = input("Pick your fighter! ")

    if computer_choice == player_choice:
        print(f"I choose {computer_choice}.")
        print("It's a tie!")
        break
    if computer_choice == "rock" and player_choice == "paper":
        print(f"I choose {computer_choice}.")
        print("You win!")
        break
    if computer_choice == "rock" and player_choice == "scissors":
        print(f"I choose {computer_choice}.")
        print("Ha, I win!")
        break
    if computer_choice == "scissors" and player_choice == "rock":
        print(f"I choose {computer_choice}.")
        print("You win!")
        break
    if computer_choice == "scissors" and player_choice == "paper":
        print(f"I choose {computer_choice}.")
        print("Ha, I win!")
        break
    if computer_choice == "paper" and player_choice == "scissors":
        print(f"I choose {computer_choice}.")
        print("You win!")
        break
    if computer_choice == "paper" and player_choice == "rock":
        print(f"I choose {computer_choice}.")
        print("Ha, I win!")
        break