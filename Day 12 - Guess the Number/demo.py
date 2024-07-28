################### Scope ####################

enemies = 1

def increase_enemies():
  enemies = 2
  print(f"enemies inside function: {enemies}")

increase_enemies()
print(f"enemies outside function: {enemies}")

# Local Scope

def drink_potion():
  potion_strength = 2
  print(potion_strength)

drink_potion()
# print(potion_strength) Error

global scope
player_health = 100

def drink_potion():
  potion_strength = 2
  print(player_health + potion_strength)

# No block scope,  if/else/for/while
if 3 > 2:
  apple = 3

print(apple)

# how to modify global variables
enemies = 0
def increase_enemies():
  global enemies
  enemies = 4
  print(enemies)

increase_enemies()
print(enemies)

# Global constants
PI = 3.14159
URL = "google.com"



  


