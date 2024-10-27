import random  # Import the random module to generate a random number.

# Greeting
play_game = input("Welcome! Do you want to play the number guessing game? (yes or no): ").strip().lower()

if play_game == "yes":  # Check if the user wants to play the game.
    # Generate a random number between 1 and 10.
    secret_number = random.randint(1, 10)
    guess = None  # Initialize guess variable.

    # Main game loop
    while guess != secret_number:
        try:
            guess = int(input("Guess a number between 1 and 10: "))  # Ask for the user's guess.
            
            if guess < secret_number:  # Provide feedback if the guess is too low.
                print("Too low. Try again!")
            elif guess > secret_number:  # Provide feedback if the guess is too high.
                print("Too high. Try again!")
            else:  # If the guess is correct.
                print("Congratulations! You've guessed the number!")
                
        except ValueError:  # Handle cases where the input is not a valid integer.
            print("Please enter a valid number.")

    # Farewell message after winning
    print("Thanks for playing! Goodbye!")

else:
    # If the user doesn't want to play
    print("Maybe next time! Goodbye!")