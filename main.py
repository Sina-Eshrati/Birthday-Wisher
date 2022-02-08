import datetime as dt
import smtplib
import pandas
import random

my_email = "sina_eshrati@yahoo.com"
my_password = "euolagjhjfqaiddm"

today = dt.datetime.now()
this_day = today.day
this_month = today.month

with open("birthdays.csv", "r") as file:
    data = pandas.read_csv(file)
    data_dict = data.to_dict()

for key, value in data_dict["day"].items():
    if this_day == value:
        if this_month == data_dict["month"][key]:
            birthday_person_name = data_dict["name"][key]
            birthday_person_email = data_dict["email"][key]
            with open(f"letter_templates/letter_{random.randint(1,3)}.txt") as file:
                template = file.read()
                letter = template.replace("[NAME]", birthday_person_name.title())
                with smtplib.SMTP_SSL("smtp.mail.yahoo.com") as connection:
                    connection.login(my_email, my_password)
                    connection.sendmail(from_addr=my_email,
                                        to_addrs=birthday_person_email,
                                        msg=f"Subject:Happy Birthday!\n\n{letter}")
