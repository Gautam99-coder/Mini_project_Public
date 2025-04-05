import random

def guess_the_number():
    # Generate a random number between 1 and 100
    secret_number = random.randint(1, 100)
    attempts = 0

    print("🎮 Welcome to the Guess the Number Game!")
    print("I'm thinking of a number between 1 and 100. Can you guess it?")

    while True:
        try:
            # Get user's guess
            guess = int(input("👉 Enter your guess: "))
            attempts += 1

            # Check if guess is correct
            if guess == secret_number:
                print(f"🎉 Congrats! You guessed it in {attempts} attempts!")
                break
            elif guess < secret_number:
                print("⬆️ Higher! Try again.")
            else:
                print("⬇️ Lower! Try again.")
        except ValueError:
            print("❌ Please enter a valid number!")

# Start the game
guess_the_number()
