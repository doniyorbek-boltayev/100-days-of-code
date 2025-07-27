def odd_or_even(number):
    if number % 2 == 0: # = was used instead of ==
        return "This is an even number."
    else:
        return "This is an odd number." 
print(odd_or_even(20))


def is_leap(year):
    if year % 4 == 0:
        if year % 100 == 0:
            if year % 400 == 0:
                return True
            else:
                return False
        elif year % 4 == 0 and year % 100 != 0:
            return True
        else:
            return False
    else:
        return False
print(f"My code: {is_leap(1600)}")

# here is more efficient version from the web
def is_leap_v02(year):
    return year % 4 == 0 and (year % 100 != 0 or year % 400 == 0)
print(f"version 2: {is_leap_v02(1600)}")

# here is another step-by-step, more logical and readable code from the web
def is_leap_v03(year):
    if year % 400 == 0:
        return True
    if year % 100 == 0:
        return False
    return year % 4 == 0

print(f"version 3: {is_leap_v03(1600)}")


# Target is the number up to which we count
def fizz_buzz(target):
    for number in range(1, target + 1):
        if number % 3 == 0 and number % 5 == 0:
            print("FizzBuzz")
        elif number % 3 == 0:
            print("Fizz")
        elif number % 5 == 0:
            print("Buzz")
        else:
            print(number)
fizz_buzz(15)
