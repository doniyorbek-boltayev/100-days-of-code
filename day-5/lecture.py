fruits = ["Apple", "Orange", "Banana"]
for fruit in fruits:
    print(fruit)
    print(fruit + " pie")
    # print(fruits)
print(fruits) # indentation matters in loops

student_scores = [87, 45, 73, 91, 60, 28, 99, 34, 76, 55, 82, 12, 68, 39, 100]

total1 = sum(student_scores)
print(f"Total socre is {total1}")
# using loops
total2 = 0
for score in student_scores:
    total2 += score
print(f"Total score is {total2}")

max1 = max(student_scores)
print(f"Maximum value in the list is {max1}")
max2 = 0
for score in student_scores:
    if score > max2:
        max2 = score
print(f"Maximum value in the list is {max2}")

# range() function with for loop
for number in range(1, 10, 3): # 10 is not inclusive
    print(number )

# add all numbers from 1 to 100 (inclusive)
total = 0
for number in range(1, 101):
    total += number
print(f"Total is {total}")

# FizzBuzz problem
for number in range(1, 101):
    if number % 3 == 0 and number % 5 == 0:
        print("FizzBuzz")
    elif number % 3 == 0:
        print("Fizz")
    elif number % 5 == 0:
        print("Buzz")
    else:
        print(number)

