print("Welcome to the rollercoaster")
height = int(input("Please input your height (in cm): "))
# conditions
if height >= 120:
    print("You can enjoy rollarcoaster!")
else:
    print("You are too short, grow up buddy ;)")

# modulus
a = 10 % 3 # a is equal to remainder
print(a)

# odd or even task

user_input = int(input("Please enter a number: "))
if user_input % 2 == 0:
    print("This number is even")
else:
    print("This number is odd")

# nested if
# elif is introduced to make matters simple while working with nested if.

print("Welcome to the rollercoaster 2.0")
height = int(input("Please input your height (in cm): "))

if height >= 120:
    print("You can enjoy rollarcoaster!")
    age = int(input("Please enter your age: "))
    if age <= 12:
        print("Please pay $5")
    elif age <= 18:
        print("Please pay $7")
    else:
        print("Please pay $12")
else:
    print("You are too short, grow up buddy ;)")


print("Welcome to the rollercoaster 3.0")
height = int(input("Please input your height (in cm): "))
bill = 0
if height >= 120:
    print("You can enjoy rollarcoaster!")
    age = int(input("Please enter your age: "))
    if age <= 12:
        bill = 5
        print("Child tickets are $5")
    elif age <= 18:
        bill = 7
        print("Teenager tickets are $7")
    elif age >= 45 and age <= 55:
        print("Have a free ticket from us!") # midlife crisis help
    else:
        bill = 12
        print("Adult tickets are $12")

    wants_photo = input("Do you want your photo to be taken ($3). Type y for Yes and n for No: ")
    if wants_photo == "y":
        bill += 3

    print(f"Your total bill is ${bill}")
else:
    print("You are too short, grow up buddy ;)")


# pizza task

print("Welcome to Pizza Deliveries!")
size = input("What size pizza do you want? S, M or L: ")
pepperoni = input("Do you want pepperoni on top of your pizza? Y or N: ")
extra_cheese = input("Do you want extra cheese on top of your pizza? Y or N: ")
bill = 0

if size == "S":
    bill += 15
elif size == "M":
    bill += 20
elif size == "L":
    bill += 25
else:
    print("There is a typo, please try again")

if pepperoni == "Y":
    if size == "S":
        bill += 2
    else:
        bill += 3
if extra_cheese == "Y":
    bill += 1

print(f"Your final bill is ${bill}")


# There are 3 basic logical operator AND, OR, NOT
