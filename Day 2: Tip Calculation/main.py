print("Welcome to the tip calculator!")
totalBill = int(input("What was the total bill? $ "))

tipPercentage = int(input("How much tip would you like to give? 10, 12, or 15? ")) / 100
people = int(input("How many people to split the bill? "))

tip = totalBill * tipPercentage
totalBill += tip

split = round(totalBill / people, 2)
print(f"Each person should pay: {split}")
