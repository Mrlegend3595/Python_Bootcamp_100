import random

names_string = input("Give me everybody's names, seperated by a comma. ")

names = names_string.split(", ") #split name and convert list

num_items = len(names) #num of elements in the list
random_choice = random.randint(0, num_items - 1)

person_who_will_pay = names[random_choice]

print(person_who_will_pay +" is going to buy the meal today.\n")

###########################way2
choice = random.choice(names) # choice 1 elements of list
print(choice +" is going to buy the meal today.(way 2 code)")