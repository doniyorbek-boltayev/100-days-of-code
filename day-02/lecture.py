
# Subscripting
print("Hello"[-1]) 

# String
print("123" + "456") # Concatenation

# Integer = Whole numbers
print(123+456)

# Large integers
print(123_456_789) # this is for us, humans, to be able to see large numbers easily. e.g. 123,456,789

# Float = Floating point numbers
print(3.14159)

# Boolean
print(True)
print(False)

print(type("Salom!"))
print(type(123))
print(type(12.03))
print(type(False))

print("Number of letter in the name: " +  str(len(input("Enter your name: "))))

print(123 + 456)
print(7 -2)
print(3 * 2)
print(6 / 3)
print(6 // 4)
print(2 ** 3)

bmi = 84 / 1.65 ** 2
print(bmi)
print(int(bmi)) # this process is called "flooring" the number. 30.875 becomes 30
print(round(bmi)) # now this round() function roundes number based on its value. If it is closer to 31 it will be 31, otherwise 29
print(round(bmi, 2)) # now new parameter, 2, is introduced to round number up to 2 decimal points

score = 0

score += 1 # this is same as score = score + 1
print(score)

# +=
# -=
# *=
# /=

score = 0
height = 1.85
is_winning = False

print(f"Your score is {score+1}")
print(f"Your height is {height}")
print(f"Is he winning? {not(is_winning)}")
