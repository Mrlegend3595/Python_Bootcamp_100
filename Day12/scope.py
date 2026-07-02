######scope########

# enemies = 1

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

# player_health = 10
# def game():
#     def drink_potion():
#         potion_strength = 2
#         print(player_health)
#
#     drink_potion() # namespace
#
# print(player_health)

#There Is No Block Scope
    #Examole1
# game_level = 3
# enemies = ["Skeleton","Zombie","Alien"]
#
# if game_level < 5:
#     new_enemy = enemies[0]
#
# print(new_enemy)

    #Exaample2
# def create_enemy():
#     game_level = 3
#     enemies = ["Skeleton","Zombie","Alien"]
#
#     if game_level < 5:
#         new_enemy = enemies[0]
#
# print(new_enemy)


# Modifying Global Scope
#Example1

# enemies = 1
#
# def increase_enemies():
#     global enemies
#     enemies += 1
#     print(f"enemies inside function Increase_enemies: {enemies}")
#
#
# increase_enemies()
# print(f"enemies outside function Increase_enemies: {enemies}")

#Example2

# enemies = 1
#
# def increase_enemies():
#     print(f"enemies inside function Increase_enemies: {enemies}")
#
# increase_enemies()
# print(f"enemies outside function Increase_enemies: {enemies}")

#Example3

# enemies = 1
#
# def increase_enemies():
#     print(f"enemies inside function Increase_enemies: {enemies}")
#     return enemies + 1
#
# enemies = increase_enemies()
# print(f"enemies outside function Increase_enemies: {enemies}")


#Global Constants

PI = 3.14159
URL = "https://www.google.com/search?q=python+calculator"
TWITTER_HANDLE = "@Yu_angela"

