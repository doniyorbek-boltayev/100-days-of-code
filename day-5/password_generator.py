import random

print("Welcome to Password Generator!")
print("How many letters would you like in your password: ", end = "")
number_of_letters = int(input())
print("How many symbols would you like in your password: ", end = "")
number_of_symbols = int(input())
print("How many numbers would you like in your password: ", end = "")
number_of_numbers = int(input())

letters = []
symbols = []
numbers = []

for index in range(number_of_letters):
    lower_or_upper = random.randint(0, 1)
    if lower_or_upper == 0:
        letter_number = random.randint(97, 122)
    else:
        letter_number = random.randint(65, 90)
    letter = chr(letter_number)
    letters.append(letter)

for index in range(number_of_symbols):
    symbol_number = random.randint(33, 43)
    while symbol_number == 34 or symbol_number == 39:
        symbol_number = random.randint(33, 43)
    symbol = chr(symbol_number)
    symbols.append(symbol)

for index in range(number_of_numbers):
    number_number = random.randint(48, 57)
    number = chr(number_number)
    numbers.append(number)

password = []
password.extend(letters)
password.extend(symbols)
password.extend(numbers)
print(password)
random.shuffle(password)
print(password)
out_string = ""
for index in range(len(password)):
    out_string += password[index]
print(f"Your password is: {out_string}")
