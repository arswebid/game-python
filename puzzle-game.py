import random

# Define the list of words for the puzzle
words = ['python', 'programming', 'algorithm', 'code']

# Choose a random word from the list
word = random.choice(words)

# Create a list to store the guessed letters
guesses = []

# Loop until the player guesses the word or runs out of guesses
while True:
    # Display the current state of the puzzle
    puzzle = ''.join([letter if letter in guesses else '_' for letter in word])
    print(puzzle)
    
    # Get a guess from the player
    guess = input("Guess a letter: ")
    
    # Check if the guess is correct
    if guess in word:
        print("Correct!")
        guesses.append(guess)
    else:
        print("Incorrect.")
    
    # Check if the player has won or lost
    if set(word) == set(guesses):
        print("Congratulations! You solved the puzzle.")
        break
    elif len(guesses) == 6:
        print("Sorry, you ran out of guesses. The word was", word)
        break
