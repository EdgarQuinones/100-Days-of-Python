# FileNotFound
# with open("file.txt") as file:
#     file.read()

# KeyError
# a_dict = {"key": "value"}
# value = a_dict["not_real_key"]

# IndexError
# num_list = [1, 2, 3]
# new_num = num_list[3]

# TypeError
# text = "abc"
# print(text + 5)

# Using Error catching

# FileNotFound
# try:
#     file = open("a_file.txt")
# except FileNotFoundError as e:
#     print(f"Error: {e}")
#     file = open("a_file.txt", "w")
#     file.write("Hi")
# except KeyError:
#     print("Key dosent exist")
# else:
#     content = file.read()
#     print(content)
# finally:
#     raise KeyError("exdddd")

# Generate your own exceptions
# height = 5
# weight = 200
#
# if height > 3:
#     raise ValueError("Human height should not be over 3 meters")
#
# bmi = weight / height ** 2
#
# print(bmi)
