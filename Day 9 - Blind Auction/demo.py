# Dictionaries
programming_dictionary = {
    "Bug": "An error in a program that prevents the program from running as expected.",
    "Function": "A piece of code that you can easily call over and over again.",
}

# # Retrieve items
print(programming_dictionary)

programming_dictionary["Loop"] = "The action of doing something over and over again"
print(programming_dictionary["Bug"])

# # # New dictionary
empty_dictionary = {}
wipe dictionary
programming_dictionary = {}
print(programming_dictionary)

# # # Edit a item
programming_dictionary["Bug"] = "Anooying things that happen"
print(programming_dictionary)

# # Loop dictionary, prints keys
for key in programming_dictionary:
    print(key)
    print(programming_dictionary[key])

# Nesting dictionaries
capitals = {
    "France": "Paris",
    "Germany": "Berlin",
}

travel_log = [
  {
    "Country": "France",
    "Cities Visited": ["Paris", "Lillie", "Dijon"],
    "total_visits": 12,
  }, 
  {
    "Germany": "Other cities",
  }
]
