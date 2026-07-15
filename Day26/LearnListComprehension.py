# numbers = [1,2,3]
# new_numbers = [number + 1 for number in numbers]
# print(new_numbers)

#--================--

# name = "Mohammadreza"
# new_list = [letter for letter in name]
# print(new_list)

#++++++++python sequence++++++++
""" list / range / string / tuple
    because it has order (iteration)
    """
#++++++++++++++++++++++++++
#challenge

# range_list = [num*2 for num in range(1,5)]
# print(range_list)

#=========================
names =["Alex", "Beth", "Caroline", "Dave", "Eleanor", "Freddie"]

short_names = [name for name in names if len(name) <= 4]
print(short_names)
#=========================
#challenge => uppercase

long_names = [name.upper() for name in names if len(name) > 4]
print(long_names)

#=========================


