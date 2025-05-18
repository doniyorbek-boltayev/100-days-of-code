print()
print("Welcome to the tip calculator!")
print("What was the total bill? ($): ", end = "")
bill = float(input())
print("What percentage of tip would you like to give.(0, 10, 15, 20): ", end = "")
tip = int(input())
print("How many people to slit the bill?: ", end = "")
num_people = int(input())

bill += bill * (tip/100)
final = bill / num_people
print(f"Each person should pay: ${final:.2f}")