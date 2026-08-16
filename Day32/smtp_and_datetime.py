# import smtplib

# my_email = ""
# password = ""

# connection = smtplib.SMTP('smtp.gmail.com', 587)
# connection.starttls()
# connection.login(user=my_email, password = password)
# connection.sendmail(from_addr = my_email, to_addrs = "test@gmail.com",
#                     msg = "Subject:Hello World\n\n"
#                           "This is body of my email.")
# connection.close()

#same Up

# with smtplib.SMTP('smtp.gmail.com', 587) as connection:
#     connection.starttls()
#     connection.login(user=my_email, password = password)
#     connection.sendmail(from_addr = my_email, to_addrs = "test@gmail.com",
#                         msg = "Subject:Davari\n\n"
#                               "Jadid_ya_Qadim ?")


#-------------------datetime--------------------
import datetime as dt

now = dt.datetime.now()

year = now.year
if year == 2026:
    print("is 2025")

month = now.month

day_of_week = now.weekday()

print(day_of_week)

date_of_birth = dt.date(year= 1995 ,month= 12 ,day= 15)
print(date_of_birth)

#----------------------------------------
