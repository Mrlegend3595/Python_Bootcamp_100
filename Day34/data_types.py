#type hints
# age : int
# name: str
# height: float
# is_human: bool

# is_human = "Yes" #this is error

#----------------------
#type hints
"""
def greeting(name : str) -> str:
    return f"Hello, {name}"
"""
def police_check(age: int) -> bool:
    if age > 18:
        can_drive = True
    else:
        can_drive = False

    return can_drive

if police_check(19):
    print("Police check is working")
else:
    print("Police check is not working")
