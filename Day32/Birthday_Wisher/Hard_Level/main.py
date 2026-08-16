##################### Hard Starting Project ######################
import datetime as dt
import pandas as pd
import random
import smtplib

SMTP_HOST_DICT = {"gmail.com":"smtp.gmail.com",
                  "yahoo.com":"smtp.mail.yahoo.com",
                  "Hotmail.com":"smtp.live.com",
                  "outlook.com":"smtp.outlook.com",
                  }

my_email = "<EMAIL>"
my_password = "<PASSWORD>"
# 1. Update the birthdays.csv with your friends & family's details.
# HINT: Make sure one of the entries matches today's date for testing purposes.

# 2. Check if today matches a birthday in the birthdays.csv
# HINT 1: Only the month and day matter.
# HINT 2: You could create a dictionary from birthdays.csv that looks like this:
# birthdays_dict = {
#     (month, day): data_row
# }

today = (dt.datetime.now().month, dt.datetime.now().day)

data = pd.read_csv("birthdays.csv")

data_dict = {(row["month"],row["day"]): row for index,row in data.iterrows()}


#HINT 3: Then you could compare and see if today's month/day matches one of the keys in birthday_dict like this:
if today in data_dict:

    letter_file = f"letter_templates/letter_{random.randint(1,3)}.txt"
    with open(letter_file) as letter :
        content = letter.read()
        content = content.replace("[NAME]" , data_dict[today]["name"])

    host = SMTP_HOST_DICT[data_dict[today]["email"].split('@')[1]]

    with smtplib.SMTP(host) as connection:
        connection.starttls()
        connection.login(my_email, my_password)
        connection.sendmail(from_addr=my_email,
                            to_addrs=data_dict[today]["email"],
                            msg=f"Subject:Happy Birthday!\n\n"
                                f"{content}")

# 3. If step 2 is true, pick a random letter from letter templates and replace the [NAME] with the person's actual name from birthdays.csv
# HINT: https://www.w3schools.com/python/ref_string_replace.asp


# 4. Send the letter generated in step 3 to that person's email address.
# HINT: Gmail(smtp.gmail.com), Yahoo(smtp.mail.yahoo.com), Hotmail(smtp.live.com), Outlook(smtp-mail.outlook.com)



