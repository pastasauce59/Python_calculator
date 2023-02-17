from art import logo
print(logo)

def add(n1, n2):
    return n1 + n2

def subtract(n1, n2):
    return n1 - n2

def multiply(n1, n2):
    return n1 * n2

def divide(n1, n2):
    return n1 / n2

operations = {
    "+": add,
    "-": subtract,
    "*": multiply,
    "/": divide
}

def calculation():
    num1 = int(input("What's the first number?: "))
    for symbol in operations:
        print(symbol)
    continue_ = True
    while continue_:
        operation_symbol = input("Pick an operation: ")
        num2 = int(input("What's the next number?: "))
        calculations_function = operations[operation_symbol]
        answer = calculations_function(num1, num2)
        
        print(f"{num1} {operation_symbol} {num2} = {answer}")
        
        keep_going = input(f"Type \"y\" to continue calculating with {answer}, or type \"n\" to start a new calculation.: ")
        if keep_going != "y":
            continue_ = False
            calculation()
        else:
            num1 = answer

calculation()