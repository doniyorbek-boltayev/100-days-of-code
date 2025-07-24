from art import logo
import random

print(logo)
print("Welcome to the Number Guessing Game!")
print("I'm thinking of a number between 1 and 100.")
number = random.randint(1, 100)
level = input("Choose a difficulty. Type 'easy' or 'hard': ")
if level == 'easy':
    attempts = 10
elif level == 'hard':
    attempts = 5
else:
    print("Error! Please type 'easy' or 'hard'")
print(f"You have {attempts} attempts remaining to guess the number.")

is_found = False
while is_found == False and attempts > 0:
    guess = int(input("Make a guess: "))
    if guess > number:
        print("Too high")
        attempts -= 1
    elif guess < number:
        print("Too low")
        attempts -= 1
    else:
        print(f"You got it! The answer was {number}")
        is_found = True
    if attempts == 0:
        print("You have lost. Run out of attempts")

# this program only works provided user inputs valid data!
