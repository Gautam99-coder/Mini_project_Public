import random

# ASCII art for visuals
ROCK = """
    _______
---'   ____)
      (_____)
      (_____)
      (____)
---.__(___)
"""

PAPER = """
     _______
---'    ____)____
           ______)
          _______)
         _______)
---.__________)
"""

SCISSORS = """
    _______
---'   ____)____
          ______)
       __________)
      (____)
---.__(___)
"""

def determine_winner(player_choice, computer_choice):
    """Decide who wins a round."""
    if player_choice == computer_choice:
        return "tie"
    elif (player_choice == "rock" and computer_choice == "scissors") or \
         (player_choice == "paper" and computer_choice == "rock") or \
         (player_choice == "scissors" and computer_choice == "paper"):
        return "player"
    else:
        return "computer"

def play_game():
    choices = {"rock": ROCK, "paper": PAPER, "scissors": SCISSORS}
    player_score = 0
    computer_score = 0

    print("\n🎮 ROCK-PAPER-SCISSORS (Best of 3) 🎮")
    print("----------------------------------")

    while player_score < 2 and computer_score < 2:
        print(f"\nScore: You {player_score} - Computer {computer_score}")

        # Player input
        player_choice = input("\nChoose: rock, paper, or scissors? ").lower()
        while player_choice not in choices:
            print("❌ Invalid choice! Try again.")
            player_choice = input("Choose: rock, paper, or scissors? ").lower()

        # Computer choice
        computer_choice = random.choice(list(choices.keys()))

        # Display choices
        print(f"\nYou chose:\n{choices[player_choice]}")
        print(f"Computer chose:\n{choices[computer_choice]}")

        # Determine winner
        result = determine_winner(player_choice, computer_choice)
        if result == "player":
            player_score += 1
            print("✅ You win this round!")
        elif result == "computer":
            computer_score += 1
            print("❌ Computer wins this round!")
        else:
            print("🤝 It's a tie!")

    # Final result
    print("\n=== GAME OVER ===")
    print(f"Final Score: You {player_score} - Computer {computer_score}")
    if player_score > computer_score:
        print("🌟 YOU WIN THE GAME! 🌟")
    else:
        print("💻 COMPUTER WINS! Better luck next time!")

# Start the game
play_game()
