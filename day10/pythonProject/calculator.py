
def mult(first, second):
    return first * second

def dev(first, second):
    return first / second

def add(first, second):
    return first + second

def minus(first, second):
    return first - second


def inputType():
    """this method takes input from a user and checks
    if it id one of the operations +-/*"""

    firstNumber = int(input("enter the first number"))
    while(True):
        # keep looping till the input is something else

        literal = input("enter the +-/* Or e to exit")
        if literal.lower() == "e":
            break

        secondNumber = int(input("enter the second number"))

        # here it should check if the input is valid
        match literal:
            case "+":
                print("+ selected")
                firstNumber = add(firstNumber, secondNumber)
                print(f"Result is {firstNumber}")
            case "-":
                print("- selected")
                firstNumber =  minus(firstNumber, secondNumber)
                print(f"Result is {firstNumber}")
            case "/":
                print("/ selected")
                firstNumber =  dev(firstNumber, secondNumber)
                print(f"Result is {firstNumber}")
            case "*":
                print("* multiply selected")
                firstNumber =  mult(firstNumber, secondNumber)
                print(f"Result is {firstNumber}")
            case _:
                print("default")
                break






if __name__ == "__main__":
    """main call"""
    inputType()