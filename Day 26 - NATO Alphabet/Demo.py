# numbers = [1, 2, 3]
# new_list = []
# for n in numbers:
#     add_1 = n + 1
#     new_list.append(add_1)

# Better Way
# numbers = [1, 2, 3]
# new_list = [n + 1 for n in numbers]
# [new_item for item in old_list]

# Other sequences
# name = 'Edgar'
# new_name = [letter for letter in name]
# print(new_name)
# new_list = [n*2 for n in range(1,5)]
# print(new_list)

# # Can include conditions
# names = ["Alex", "Beth", "Dave", "Caroline", "Edgar"]
# new_list = [item for item in names if len(item) <= 4]
# print(new_list)
# names = ["Alex", "Beth", "Dave", "Caroline", "Edgar"]
# new_list = [item.upper() for item in names if len(item) >= 5]
# print(new_list)

# Can do this with dictionaries as well
# import random
#
# names = ["Alex", "Beth", "Dave", "Caroline", "Edgar"]
# random_scores = {student: random.randint(0, 100) for student in names}
# # Key: Item for item in list
#
# past_students = {student: score for (student, score) in random_scores.items() if score >= 60}
#
# # print(random_scores)
# print(past_students)

# How to iterate over a Pandas DataFrame
student_dict = {
    "student": ["Angela", "James", "Lily"],
    "score": [56, 76, 98],
}

# Looping through dictionaries:
# for (key, value) in student_dict.items():
#     print(value)

# import pandas
#
# student_data_frame = pandas.DataFrame(student_dict)
# # print(student_data_frame)
#
# # Loop through a data frame
# for (index, row) in student_data_frame.iterrows():
#     if row.student == "Angela":
#         print(row.score)
