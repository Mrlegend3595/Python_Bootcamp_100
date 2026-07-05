# print("| Pokemon Name | Type |")
# print("_______________________")


#pypi.org
#install Package Setting=>project=>Interpreter
#or terminal: pip install {package_name}


from prettytable import PrettyTable

#challenege: make class of prettytable

table = PrettyTable()

#challenge :add information to this table

table.add_column("Pokemon Name", ["Pikachu", "Squirtle", "Charmander"])
table.add_column("Type",["Electric", "Water", "Fire"])


#challenge: center align => left align
table.align = "l"

print(table)



