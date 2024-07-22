#Password Generator Project
import random
letters = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z', 'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']
numbers = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
symbols = ['!', '#', '$', '%', '&', '(', ')', '*', '+']

print("Welcome to the PyPassword Generator!")
nr_letters= int(input("How many letters would you like in your password? ")) 
nr_symbols = int(input(f"How many symbols would you like? "))
nr_numbers = int(input(f"How many numbers would you like? "))

# Easy Password Calculations

# add letters 
letter_portion = ""
for random_letter in range(0, nr_letters):
    letter_portion += letters[random.randint(0,len(letters)-1)]
letter_portion_size = len(letter_portion)

# add symbols 
symbol_portion = ""
for random_symbol in range(0, nr_symbols):
    symbol_portion += symbols[random.randint(0,len(symbols)-1)]
symbol_portion_size = len(symbol_portion)

# add numbers 
number_portion = ""
for random_number in range(0, nr_numbers):
    number_portion += numbers[random.randint(0,len(numbers)-1)]
number_portion_size = len(number_portion)

easy_password = letter_portion + symbol_portion + number_portion

# Hard Password Calculations 

total_portion_size = letter_portion_size + symbol_portion_size + number_portion_size
combined_portions = letter_portion + symbol_portion + number_portion

list_of_portions = []
for number in range(0,len(combined_portions)):
    list_of_portions.append(combined_portions[number])

hard_password = ""

for intervals in range(0, total_portion_size):
    if len(list_of_portions) > 1:
        random_index = random.randint(0, len(list_of_portions) - 1)
        hard_password += list_of_portions.pop(random_index)
    else:
        hard_password += list_of_portions.pop()


#Eazy Level - Order not randomised:
#e.g. 4 letter, 2 symbol, 2 number = JduE&!91

print(f"Here is your easy password: {easy_password}")

#Hard Level - Order of characters randomised:
#e.g. 4 letter, 2 symbol, 2 number = g^2jk8&P

print(f"Here is your hard password: {hard_password}")
