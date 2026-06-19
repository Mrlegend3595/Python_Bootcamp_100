programming_dictionary = {
    "Bug": "logic error",
    "function": "a block of code that can repeat",
    }

#print(programming_dictionary["Bug"])
#print(programming_dictionary["Bog"]) error
#print(programming_dictionary[Bug]) error

"""problems
    KeyError: type dont correct
    از نوع داده سحيح نميشه استفاده کرد به عنوان کليد
    """

#add new item
#programming_dictionary["conditions"] = "if and else"
#print(programming_dictionary)

# empty dictionary
#empty_dictionary = {}

#wipe an existing dict
#programming_dictionary = {}
#print(programming_dictionary)

#Edit item in dict
#programming_dictionary["Bug"] = "A moth in your computer"
#print(programming_dictionary["Bug"])

# loop thrugh dict
for key in programming_dictionary:
    print(key) #just give you key
    print(programming_dictionary[key])
    
