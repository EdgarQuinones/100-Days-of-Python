# Calculator

from art import logo

# Add
def add(n1,n2):
    return n1 + n2

# Subtract
def subtract(n1,n2):
    return n1 - n2

# Multiply
def multiply(n1,n2):
    return n1 * n2

# Divide
def divide(n1,n2):
    return n1 / n2

operations = {
    "+" : add,
    "-" : subtract,
    "*" : multiply,
    "/" : divide,
}

print(logo)

done_calculating = False
new_calculation = False
num1 = 0
while not done_calculating:
    
    if not new_calculation:
        num1 = float(input("What's the first number? "))
        
    for operation in operations:
        print(operation)
    operation = input("What's the operation? ")
    
    num2 = float(input("What's the next number? "))
    
    calculation_function = operations[operation]
    answer = calculation_function(num1,num2)
    
    print(f"{num1} {operation} {num2} = {answer}")

    reply = input(f"Options: 'y' to continue with {answer}, 'n' for new calculation, or 'q' to end program\n").lower()
    new_calculation = False
    if reply == "y":
        new_calculation = True
        num1 = answer
    elif reply == "n":
        continue
    else:
        print("Bye.")
        break
    
