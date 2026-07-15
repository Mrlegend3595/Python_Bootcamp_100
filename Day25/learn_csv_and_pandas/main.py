#----------------CSV-----------------------

#challenge 1
# with open("weather_data.csv") as data_file:
#     data = data_file.readlines()
#     print(data)


# import csv
#
# with open("weather_data.csv") as data_file:
#     data = csv.reader(data_file)
#     # print(data) #Output is object of csv
#     #challenge 2
#     temperatures = []
#     for row in data:
#         if row[1] != "temp":
#             temperatures.append(int(row[1]))
#
#     print(temperatures)

#----------------PANDAS---------------------
import pandas as pd

# data = pd.read_csv("weather_data.csv")
# print(data)
# print("--------------------------")
# #challenge 2 with pandas. that is easier than csv
# print(data["temp"])

#-------------------dataframe and series-----------------------
# print(type(data)) #this is a data frame. all the table. any page sheets are data frame.
# print(type(data["temp"])) #This is a serie. A column of table like a list.
#
# data_dict = data.to_dict()
# print(data_dict)
#
# #challenge 2 easier
# temp_list = data["temp"].tolist()
# print(temp_list)

#--------------challenge 3 _ Mean ------------------
#my way
# s = data["temp"].sum()
# n = data["temp"].count()
# ave = s/n
# print(ave)

#solution
# temp_list = data["temp"].tolist()
# average = sum(temp_list)/len(temp_list)
# print(average)
#
# #easier solution
# print(data["temp"].mean())

#-------------------print max of serie------------
# print(data["temp"].max())

#-----------Get Data in Columns--------------
# print(data["condition"])
#
# print(data.condition)#same up.

#-----------Get Data in Row------------------
# print(data[data.day == "Monday"])
#
# #-----------challenge 4 ---------
# print(data[data.temp == data["temp"].max()])
#
# #------------access to values of row-----
# monday = data[data.day == "Monday"]
# print(monday.condition)
# #--------challenge 5-------------
# monday_temp = int(monday.temp)# without error must be monday.temp[0]
# f = (1.8 * monday_temp) + 32
# print(f)








#----------create a dataframe from scratch ---
data_dict = {
    "students":["Amy", "James", "Angela"],
    "scores":[76, 56, 65],
}
data = pd.DataFrame(data_dict)
data.to_csv("new_data.csv")


