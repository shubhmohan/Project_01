def win_check(player, computer):
    if player == computer:
        return "Tie"
    elif (player == "scissor" and computer == "paper") or \
         (player == "paper" and computer == "rock") or \
         (player == "rock" and computer == "scissor"):
        return "Player wins"
    
    else:
        return "Computer wins"
        

import random

def comp_choice():
    choices = ["scissor", "paper", "rock"]
    return random.choice(choices)

def user_choice():
    choice = input("Enter your choice (scissor, paper, rock): ").lower()
    while choice not in ["scissor", "paper", "rock"]:
        print("Invalid choice. Please try again.")
        choice = input("Enter your choice (scissor, paper, rock): ").lower()
    return choice

def score():
    player_score = 0
    computer_score = 0
    rounds = int(input("Enter the number of rounds to play: "))

    for _ in range(rounds):
        player = user_choice()
        computer = comp_choice()
        print(f"Computer chose: {computer}")
        
        result = win_check(player, computer)
        print(result)
          
        if result == "Player wins":
            player_score += 1
        elif result == "Computer wins":
            computer_score += 1
            
            
    print(f"Final Score - Player: {player_score}, Computer: {computer_score}")
    if player_score > computer_score:
        print("🎉 You won the game!")
    elif player_score < computer_score:
        print("💻 Computer won the game!")
    else:
        print("🤝 It's a tie!")

def play_game():
    print("Welcome to Rock Paper Scissors Game!")
    score()
    print("Thanks for playing!")

def play_again():
    while True:
        again = input("Do you want to play again? (yes/no): ").lower()
        if again == "yes":
            play_game()
        elif again == "no":
            print("Thanks for playing! Goodbye!👋")
            break
        else:
            print("Invalid input. Please enter 'yes' or 'no'.")    


#Start the game
name= input("Enter your name: ")
print(f"Hello {name}, let's start the game!")
play_game()
play_again()

