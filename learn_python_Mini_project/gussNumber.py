import random
import time

def number_guessing_game():
    print("Welcome to the Number Guessing Game!")
    print("I'm thinking of a number between 1 and 100.")
    
    # Generate random number
    secret_number = random.randint(1, 100)
    attempts = 0
    max_attempts = 10
    score = 100  # Starting score that decreases with each attempt
    
    # Difficulty selection
    print("\nSelect difficulty:")
    print("1. Easy (10 attempts)")
    print("2. Medium (7 attempts)")
    print("3. Hard (5 attempts)")
    
    difficulty = input("Enter difficulty (1-3): ")
    if difficulty == '1':
        max_attempts = 10
    elif difficulty == '2':
        max_attempts = 7
    elif difficulty == '3':
        max_attempts = 5
    else:
        print("Invalid choice. Defaulting to Medium difficulty.")
        max_attempts = 7
    
    print(f"\nYou have {max_attempts} attempts to guess the number.")
    
    while attempts < max_attempts:
        attempts += 1
        remaining_attempts = max_attempts - attempts + 1
        
        try:
            guess = int(input(f"\nAttempt {attempts}/{max_attempts}. Enter your guess: "))
        except ValueError:
            print("Please enter a valid number!")
            attempts -= 1  # Don't count invalid attempts
            continue
        
        if guess == secret_number:
            print(f"\nCongratulations! You guessed the number in {attempts} attempts!")
            print(f"Your score: {max(0, score - (attempts-1)*10)}/100")
            time.sleep(2)
            play_again()
            return
        elif guess < secret_number:
            print(f"Too low! (Remaining attempts: {remaining_attempts - 1})")
        else:
            print(f"Too high! (Remaining attempts: {remaining_attempts - 1})")
    
    print(f"\nGame over! The number was {secret_number}.")
    time.sleep(2)
    play_again()

def play_again():
    choice = input("\nWould you like to play again? (y/n): ").lower()
    if choice == 'y':
        number_guessing_game()
    else:
        print("Thanks for playing! Goodbye!")

if __name__ == "__main__":
    number_guessing_game()
