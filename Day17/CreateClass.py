#Create class
# class User:
#     pass
#
# #Create an object of class
# user1 = User()
#
# #add attribute to class
# user1.id = "001"
# user1.username = "John"
#
# print(user1.username)
#
# user_2 = User()
# user_2.id = "002"
# user_2.username = "Mohammad"
# print(user_2.username)

#Do we always have to write all these
#repetitive lines to create multiple objects
# and initialize them?
################################################
# What is Constructor ?
"""It causes a method to execute when an object
is instantiated from the class—performing
initialization—or ensures that any
instructions within that method are run at
the time of object creation."""

#Create Class
# class User:
#     #The word "self" refers to the object itself.
#     def __init__(self, user_id, username):
#         self.id = user_id
#         self.username = username
#         #Create attribute with default value.
#         #A property with a default value does
#         #not appear in the constructor parameters.
#         self.followers = 0
#         print("new user being created...")
#
# user1 = User("001","angela")
#
# print(user1.id)
# print(user1.username)
# print(user1.followers)

# run below with error
# user_2 = User()
# user_2.id = "002"
# user_2.username = "Mohammad"
# print(user_2.username)


##########################################
#add methode

class User:
    def __init__(self, user_id, username):
        self.id = user_id
        self.username = username
        self.followers = 0
        self.following = 0
        print(f"new user being created...{self.id}")

    #create methode follow
    def follow(self, user):
        user.followers += 1
        self.following += 1


user1 = User("001","angela")
user2 = User("002","john")

user1.follow(user2)
print(user1.followers)
print(user1.following)
print(user2.followers)
print(user2.following)

