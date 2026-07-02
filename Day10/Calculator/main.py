from art import logo
#Calculator

#Add
def add(n1, n2):
    """Adds two numbers together"""
    return n1 + n2

#substract
def subtract(n1, n2):
    """Subtracts two numbers together"""
    return n1 - n2

#multiply
def multiply(n1, n2):
    """Multiplies two numbers together"""
    return n1 * n2

#divide
def divide(n1, n2):
    """Divides two numbers together"""
    return n1 / n2

#save function as object function, no store func() because this is run function
operations = {
    "+": add,
    "-": subtract,
    "*": multiply,
    "/": divide,
}

def calculator():
    print(logo)

    num1 = float(input("What's the first number?: "))

    for symbol in operations:
        print(symbol)

    should_continue = True

    while should_continue:
        operation_symbol = input("Pick an operation: ")

        num2 = float(input("What's the next number?: "))

        #save function object in variable and calling variable with argument because variable is function object __call__
        calculation_function = operations[operation_symbol]
        answer = calculation_function(num1, num2)

        print(f"{num1} {operation_symbol} {num2} = {answer}")

        if input(f"Type 'y' to continue calculating with {answer}, or type 'n' to start a new calculation.: ") == 'y':
            num1 = answer
        else:
            should_continue = False
            calculator()


calculator()