#Challenge 1

# number = int(input("Which number do you want to check? "))
# if number % 2 = 0: #solution | = wrong . == true
#     print("This is even number.")
# else:
#     print("This is odd number.")


#Challenge 2

# year = input("Which year do you want to check?") #solution | convert to int
#
# if year % 4 == 0:
#     if year % 100 == 0:
#         if year % 400 == 0:
#             print("Leap year.")
#         else:
#             print("Not a leap year.")
#     else:
#         print("Leap year.")
# else:
#     print("Not a leap year.")



#challenge 3

for number in range(1,101):
    if number % 3 == 0 or number % 5 == 0: # 'or' is wrong . true is 'and'
        print("FizzBuzz")
    if number % 3 == 0: # if wrong ==> elif
        print("Fizz")
    if number % 5 == 0:# if wrong ==> elif
        print("Buzz")
    else:
        print([number]) # remove []
