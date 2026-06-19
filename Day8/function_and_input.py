#simple function
# def greet():
#     print("Hello")
#     print(f"How do you do?")
#     print("Isn't the weather nice today?\n")



#function that allows for input
# def greet_with_name(name):
#     print(f"Hello {name}")
#     print(f"How do you do {name}?")
#     print("Isn't the weather nice today?")

#function with more than 1 input
def greet_with(name, location):
    print(f"Hello {name}")
    print(f"What is it like in {location}?")

greet_with("Mohammad","Austria")

#positional argument
greet_with("Austria","Mohammad") #this is problem. position is important. What should I do?

#keyword argument
greet_with(location= "Austria", name= "Mohammad")#good




