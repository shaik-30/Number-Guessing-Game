import random

def play_game():
    print("=== Number Guessing Game ===")
    number = random.randint(1, 50)
    attempts = 0
    max_attempts = 10

    print("I have chosen a number between 1 and 100.")
    print("You have 10 attempts to guess it.\n")

    while attempts < max_attempts:
        guess = input(f"Attempt {attempts+1}: Enter your guess: ")

        if not guess.isdigit():
            print("❌ Please enter a number only.")
            continue

        guess = int(guess)
        attempts += 1

        if guess == number:
            print(f"🎉 Congratulations! You guessed the number in {attempts} attempts.")
            return
        elif guess < number:
            print("Too low!")
        else:
            print("Too high!")

    print(f"\nSorry! The number was {number}. Better luck next time!")

# Run the game
play_game()
