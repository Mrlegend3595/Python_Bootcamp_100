#FileNotFound
# with open("file.txt") as file:
#     file.read()

#KeyError
# a_dictionary = {"key": "value"}
# value = a_dictionary["non_existing"]


#IndexError
# fruit_list = ['apple', 'banana', 'orange', 'strawberry']
# fruit = fruit_list[3]

#TypeError
# text = 'abc'
# print(text + 5)


################################

#
# try:
#     file = open("a_file.txt")
#     a_dictionary = {"key" : "value"}
#     print(a_dictionary["es"])
# except FileNotFoundError:
#     file = open("a_file.txt", "w")
#     file.write("something")
# except KeyError as error_message:
#     print("That key doesn't exist: ", error_message)
# else:
#     content = file.read()
#     print(content)
# finally:
#     file.close()
#     print("File has been closed")


#**********************************

height = float(input("Enter your height in meters: "))
weight = int(input("Enter your weight in kilograms: "))
if height > 3:
    raise ValueError("Height must not be greater than 3")
bmi = weight / (height ** 2)
