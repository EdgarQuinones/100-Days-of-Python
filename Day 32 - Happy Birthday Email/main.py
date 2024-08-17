# import smtplib
#
# my_email = "email sender"
# my_password = "app password"
#
# with smtplib.SMTP("smtp.gmail.com", port=587) as connection:
#     connection.starttls()
#     connection.login(user=my_email, password=my_password)
#     connection.sendmail(from_addr=my_email,
#                         to_addrs="other email",
#                         msg="Subject:Hi from python\n\nThis is the body lol!")

# import datetime as dt
#
# now = dt.datetime.now()
# year = now.year
# print(year)
#
# data_of_birth = dt.datetime(year=1995, month=2, day=14)

import datetime as dt
import smtplib
import random

with open("quotes.txt") as file:
    quotes = file.readlines()

current_day = dt.datetime.now()
day_of_the_week = current_day.weekday()

if day_of_the_week == 5:
    my_email = "email sender"
    my_password = "app password"

    with smtplib.SMTP("smtp.gmail.com", port=587) as connection:
        connection.starttls()
        connection.login(user=my_email, password=my_password)
        connection.sendmail(from_addr=my_email,
                            to_addrs="other email",
                            msg=f"Subject:Hi from python\n\n{random.choice(quotes)}")
