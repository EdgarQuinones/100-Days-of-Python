############DEBUGGING#####################

# Describe Problem
def my_function():
  for i in range(1, 21):
    if i == 20:
      print("You got it")
my_function()
# PROBLEM: Range ends at 19, not 20

# Reproduce the Bug
from random import randint
dice_imgs = ["❶", "❷", "❸", "❹", "❺", "❻"]
dice_num = randint(1, 6)
print(dice_imgs[dice_num])
# PROBLEM: INDEX ERROR 0-5

# Play Computer
year = int(input("What's your year of birth?"))
if year > 1980 and year < 1994:
  print("You are a millenial.")
elif year > 1994:
  print("You are a Gen Z.")
# PROBLEM: Nothing prints before 1980, and should add equals

# Fix the Errors
age = input("How old are you?")
if age > 18:
    print(f"You can drive at age {age}.")
# FORGOT f FOR f-string, AND THE INDENT, and int casting

#Print is Your Friend
pages = 0
word_per_page = 0
pages = int(input("Number of pages: "))
word_per_page = int(input("Number of words per page: ")) # SHOULD BE EQUAL
total_words = pages * word_per_page
print(total_words)

#Use a Debugger
def mutate(a_list):
  b_list = []
  for item in a_list:
    new_item = item * 2
    b_list.append(new_item) # DIDNT INDENT
  print(b_list)

mutate([1,2,3,5,8,13])
