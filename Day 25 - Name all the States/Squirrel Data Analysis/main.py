# with open("weather_data.csv", mode="r") as file:
#     content = file.readlines()
#
# for index in range(len(content)):
#     content[index].strip()
#
# print(content)

# import csv
#
# with open("weather_data.csv") as data_file:
#     data = csv.reader(data_file)
#     temp_column = 1
#     temperatures = []
#     for row in data:
#         if row[temp_column] != "temp":
#             temperatures.append(int(row[temp_column]))
# print(temperatures)

# import pandas
#
# data = pandas.read_csv("weather_data.csv")
# print(type(data))
# print(type(data["temp"]))

# data_dict = data.to_dict()
# print(data_dict)

# temp_list = data["temp"].to_list()
# print(temp_list)
#
# print(data.temp.max())

# print(data[data.temp == data.temp.max()])
# monday = data[data.day == "Monday"]
# print(monday.temp * 9/5 + 32)

# data = pandas.DataFrame(data)
# data.to_csv()

import pandas

#
data = pandas.read_csv("2018_Central_Park_Squirrel_Census_-_Squirrel_Data.csv")

black = len(data[data["Primary Fur Color"] == "Black"])
cinnamon = len(data[data["Primary Fur Color"] == "Cinnamon"])
gray = len(data[data["Primary Fur Color"] == "Gray"])

new_data = {
    "Color": ["gray", "black", "cinnamon"],
    "Count": [gray, black, cinnamon],

}

new_file = pandas.DataFrame(new_data)
new_file.to_csv("Sq_count")
