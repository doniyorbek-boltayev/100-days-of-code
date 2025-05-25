import urllib.request
import random
from hangman_art import stages

word_site = "https://www.mit.edu/~ecprice/wordlist.10000"
response = urllib.request.urlopen(word_site)
txt = response.read()
WORDS = txt.splitlines()
WORDS = [word.decode('utf-8') for word in WORDS]


lives = 6 # Start with 6 lives
goal_word = random.choice(WORDS).lower() # Randomly choose a word and convert to lowercase
raw_word = ["_"] * len(goal_word)
guessed_letters = [] # To keep track of all guessed letters

print("Welcome to Hangman!")
while lives > 0 and "".join(raw_word) != goal_word:
    # Print the current hangman picture
    print(stages[6 - lives]) # 6 - lives will give the correct index for lives lost

    print(f"\nWord to guess: {' '.join(raw_word)}")
    print(f"Guessed letters: {', '.join(sorted(guessed_letters))}") # Display guessed letters
    print(f"Lives left: {lives}")

    guess = input("Guess a letter: ").lower() # Convert guess to lowercase

    if len(guess) != 1 or not guess.isalpha():
        print("Please enter a single letter.")
        continue # Ask for input again

    if guess in guessed_letters:
        print(f"You already guessed '{guess}'. Try a different letter.")
        continue # Ask for input again

    guessed_letters.append(guess) # Add the current guess to the list of guessed letters

    if guess in goal_word:
        print(f"You guessed '{guess}'. It was correct!")
        for index, letter in enumerate(goal_word):
            if letter == guess:
                raw_word[index] = guess
    else:
        lives -= 1
        print(f"You guessed '{guess}'. It was incorrect. You lose a life!")

# Game End
print(stages[6 - lives]) # Print the final hangman picture
if "".join(raw_word) == goal_word:
    print(f"\nCongratulations! You guessed the word: {goal_word}")
else:
    print("\nGame Over! You ran out of lives.")
    print(f"The word was: {goal_word}")
