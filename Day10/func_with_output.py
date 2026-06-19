#already used function with outputs.
length = len("Hello, world!")

#function with return value
#return as an early exit
def format_name(f_name, l_name):
    """Take a first and last name and format it to return
     the title case version of the name."""
    #this is in above : docstring
    if f_name == "" or l_name =="":
        return "You didn't provide valid input."
    formated_f_name = f_name.title()
    formated_l_name = l_name.title()
    return f"Result : {formated_f_name} {formated_l_name}"

print(format_name(input("What is your first name? "), input("What is your last name? ")))


"""This 
is
 a
  comment"""

# this
# is
# a
# comment
#ctrl + /    is comment multi line


a = """this is not comment! assign to variable"""