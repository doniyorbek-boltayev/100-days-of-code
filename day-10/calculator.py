import os

def add(n1, n2):
    """Adds two numbers together"""
    return n1 + n2

def subtract(n1, n2):
    """Subtracts n2 from n1"""
    return n1 - n2  

def multiply(n1, n2):
    """Multiply two numbers"""
    return n1 * n2

def divide(n1, n2):
    """Divide n1 by n2"""  
    if n2 == 0:
        return "Error: Cannot divide by zero"
    return n1 / n2

operations = {
    '+': add,
    "-": subtract,
    "*": multiply,
    "/": divide,
}

def get_operation():
    """Get a valid operation from user"""
    while True:
        operation = input("Which arithmetic operation do you want to perform? +, -, *, /: ")
        if operation in operations:
            return operation
        print("Invalid operation! Please choose +, -, *, or /")

def calculate():
    """Perform a calculation"""
    try:
        first_num = float(input("Enter the first number: "))
        operation = get_operation()
        second_num = float(input("Enter the second number: "))
        
        result = operations[operation](first_num, second_num)
        print(f"{first_num} {operation} {second_num} = {result}")
        return result
    except ValueError:
        print("Error: Please enter valid numbers")
        return None

print("Welcome to the calculator!")

result = None
while True:
    if result is None:
        # Start fresh calculation
        result = calculate()
        if result is None:
            continue
    else:
        # Continue with previous result
        print(f"Current result: {result}")
        operation = get_operation()
        try:
            second_num = float(input("Enter the second number: "))
            result = operations[operation](result, second_num)
            print(f"Result: {result}")
        except ValueError:
            print("Error: Please enter a valid number")
            continue
    
    # Get user choice
    while True:
        choice = input("Type 'yes' to continue with result, 'no' for new calculation, 'end' to quit: ").lower()
        if choice in ['yes', 'no', 'end']:
            break
        print("Please type 'yes', 'no', or 'end'")
    
    if choice == 'end':
        print("Thanks for using the calculator!")
        break
    elif choice == 'no':
        os.system('cls')
        result = None
