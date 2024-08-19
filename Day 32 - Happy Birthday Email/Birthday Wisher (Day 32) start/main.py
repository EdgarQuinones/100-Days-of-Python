##################### Normal Starting Project ######################


import datetime as dt
import random
import smtplib

import pandas

now = dt.datetime.today()

data = pandas.read_csv("birthdays.csv")
persons = data.to_dict(orient="records")

for person in persons:
    year = int(person["year"])
    month = int(person["month"])
    day = int(person["day"])

    if year == now.year and month == now.month and day == now.day:
        print(f"It is {person["name"]}'s birthday!")
        random_number = random.randint(1, 3)
        random_letter = f"letter_templates/letter_{random_number}.txt"

        with open(random_letter, mode="r") as file:
            new_file = file.read()
            new_file = new_file.replace("[NAME]", person["name"])

        print(new_file)

my_email = "email"
my_password = "password"

with smtplib.SMTP("smtp.gmail.com", port=587) as connection:
    connection.starttls()
    connection.login(user=my_email, password=my_password)
    connection.sendmail(from_addr=my_email,
                        to_addrs=my_email,
                        msg=f"Subject:Happy Birthday!\n\n{new_file})")
