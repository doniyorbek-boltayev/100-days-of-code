
rock = ("""
    _______
---'   ____)
      (_____)
      (_____)
      (____)
---.__(___)
""")

paper = ("""
     _______
---'    ____)____
           ______)
          _______)
         _______)
---.__________)
""")


scissors = ("""
    _______
---'   ____)____
          ______)
       __________)
      (____)
---.__(___)
""")

import random

print("What do you choose? Type 0 for Rock, 1 for Paper or 2 for Scissors")
user_choice = int(input())
print("Your choice: ")
if user_choice == 0:
    print(rock)
elif user_choice == 1:
    print(paper)
elif user_choice == 2:
    print(scissors)
else:
    print("Invalid input! Please try again")

print("Computer's choice: ")
computer_choice = random.randint(0, 2)
if computer_choice == 0:
    print(rock)
elif computer_choice == 1:
    print(paper)
else:
    print(scissors)



if user_choice == 0 and computer_choice == 1:
    print("Computer won")
elif user_choice == 0 and computer_choice == 2:
    print("You won")
elif user_choice == 1 and computer_choice == 0:
    print("You won")
elif user_choice == 1 and computer_choice == 2:
    print("Computer won")
elif user_choice == 2 and computer_choice == 0:
    print("Computer won")
elif user_choice == 2 and computer_choice == 1:
    print("You won")
else:
    print("Draw")
