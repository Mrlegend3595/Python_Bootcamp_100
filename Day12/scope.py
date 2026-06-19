######scope########

enemies = 1

# def increase_enemies():
#     enemies = 2
#     print(f"enemies inside function Increase_enemies: {enemies}")
#
#
# increase_enemies()
# print(f"enemies outside function Increase_enemies: {enemies}")

#Local scope

# def drink_potion():
#     potion_strength = 2
#     print(potion_strength)
#
# drink_potion()
# print(potion_strength)

#Global Scope

player_health = 10
def game():
    def drink_potion():
        potion_strength = 2
        print(player_health)

    drink_potion() # namespace

print(player_health)