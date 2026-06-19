states_of_america = ["Delaware","Pensnsylvania"]

print(states_of_america)

print(states_of_america[0])

print(states_of_america[-1])

print(states_of_america[-2])


states_of_america[0] = "pencil"
print(states_of_america)


states_of_america.append("hawaii")
print(states_of_america)

states_of_america.append(["kawaiii" , "canada"])
print(states_of_america)

states_of_america.extend(["lala land" , "Iran"])
print(states_of_america)


num_of_states = len(states_of_america)
print(states_of_america[num_of_states - 1])# len - 1 correct , len not

############################################ nested list

#dirty_dozen = ["Strawbarries", "Spinach", "Kale", "Nectarines", "Apples", "Grapes", "Peaches", "Cherries", "Pears", "Tomatoes", "Celery", "Potatoes"]
fruits = ["Strawbarries","Nectarines","Apples", "Grapes", "Peaches", "Cherries", "Pears"]
vegetables = ["Spinach", "Kale", "Tomatoes", "Celery", "Potatoes"]

dirty_dozen = [fruits , vegetables]
print(dirty_dozen)


