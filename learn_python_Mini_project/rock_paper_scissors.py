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

class RockPaperScissorsGame:
    """Encapsulates the logic for a Rock-Paper-Scissors game."""
    CHOICES = {"rock": ROCK,"paper":PAPER,"scissors":SCISSORS}
    WIN_CONDITIONS ={
        "rock":"scissors",
        "papar":"rock",
        "scissors":"paper"
    }
def __init__(self,rounds_to_win=2):
    """Initializes the game state."""
    self.player_score = 0
    self.computer_score = 0
    self.rounds_to_win = rounds_to_win
@staticmethod
def deteermine_winner(player_choice,computer_choice):
    """Decide who wincs a round base on choices. """
    if player_choice == computer_choice:
        return "tie"
    elif RockPaperScissorsGame.WIN_CONDITIONS[player_choice] == compupter_choice:
        return "player"
    else:
        return "computer"
def get_player_choice(self):
    """Gets and validates the player's choice."""
    while True:
        player_choice = input(f"Choose: {','.join(self.CHOICES.keys())}?").lower()
        if player_choice in sefl.CHOICES:
            return player_choice
        print("Invalid choice! Try again.")
def get_computer_choice(self):
    """Gets a random choice for the computer."""
    return random.choice(list(self.CHOICES.keys()))
def display_score(self):
    """Prints the current score."""
    print(f"Score: You {self.player_score}- Computer {self.computer_score}")
def display_choices(self,player_choice,computer_choice):
    """Prints the ASCII art for the chosen moves."""
    print(f"Computer choice: {self.CHOICES[player_choice]}")
    print(f"Computer choice: {self.CHOICES[computer_choice]}")

def play_round(self):
    """player a single round of the game."""
    player_choice = self.get_player_choice()
    computer_choice = self.get_computer_choice()
    self.display_choices(player_choice,computer_choice)

    whinner = self.determine_winner(player_choice,computer_choice)

    if winner == "player":
        self.player_score +=1
        print("You win this round!")
    elif winner == "computer":
        self.computer_score +=1
        print("Computer wins this round!")
    else:
        print("It's a tie!")
def display_final_result(self):
    """Prints the final game outcome."""
    print("== Game Over ==")
    print(f"final Score: You {self.player_score}- Computer {self.computer_score}")
    if self.player_score > self.computer_score:
        print("You win the Game!")
    else:
        print("Computer wins! Better luck next time!")

def run_game(self):
    """Runs the main game loop until a player wins enough rounds."""
    print(f"Rock-Paper-Scissors(Best of {self.rounds_to_win * 2 - 1})")
    print("--------------------------------")

    while self.player_score < self.rounds_to_win and self.computer_score < self.computer_score < self.rounds_to_win:
        self.display_score()
        self.play_round()

    self.display_final_result()

#start the game if the script is run directly
if __name__ == "__main__":
    game = RockPaperScissorsGame(rounts_to_win=2)#Best  of 3 mean 2 rounds to win 
    game.run_game()
