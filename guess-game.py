import random

# Generate a random number between 1 and 10
number = random.randint(1, 10)

# Set the initial number of guesses to 0
guesses = 0

# Loop until the user guesses the number or runs out of guesses
while guesses < 3:
    # Get a guess from the user
    guess = int(input("Guess a number between 1 and 10: "))
    
    # Increment the number of guesses
    guesses += 1
    
    # Check if the guess is correct
    if guess == number:
        print("Congratulations! You guessed the number in", guesses, "guesses.")
        break
    elif guess < number:
        print("Too low. Guess again.")
    else:
        print("Too high. Guess again.")
else:
    print("Sorry, you ran out of guesses. The number was", number)
