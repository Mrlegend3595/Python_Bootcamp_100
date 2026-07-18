# #Argument with default values
# #positional argument and keyword argument
# #default argument
# def my_func(a, b=2, c=3):
#     return a + b + c
# print(my_func(3))
# #Advanced python Argument:
#
# #unlimited argument
# def add(*args):
#     for arg in args: #args is a tuple
#         print(arg)
#
# add(5,3)


#=========challenge1============
def add(*args):
    #args[0]
    sum = 0
    for n in args:
        sum += n
    return sum
#unlimited positional argument
print(add(1,2,3,4,5))

#=========Many keyworded arguments=========

def calculate(n, **kwargs): # kwargs is a dict for use a key:value format
    print(kwargs)
    # for key, value in kwargs.items():
    #     print(key)
    #     print(value)

    # print(kwargs["add"])

    n += kwargs["add"]
    n += kwargs["multiply"]

calculate(2, add=3, multiply=5)


class Car:
    def __init__(self, **kwargs):
        self.color = kwargs.get("color")
        self.model = kwargs.get("model")
        self.make = kwargs.get("make")
        self.year = kwargs.get("year")
        self.seats = kwargs.get("seats")
        self.autodrive = kwargs.get("autodrive")

toyota = Car(make="Nissan",model="GT-R",year=2019,seats=4)
print(toyota.color)
print(toyota.model)
print(toyota.year)
