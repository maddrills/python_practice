num1 = input("first number")
num2 = input("second number")


# throw an error if the input isent valid
try:
    print(int(num1) * int(num2))
except:
    print("An error occurred")