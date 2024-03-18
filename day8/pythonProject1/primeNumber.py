def checkPrime(number):

    # check
    if number < 1:
        return "Not a valid input"
    if number < 2:
        return "Not a prime"

    for i in range(2, number - 1):
        # check if number is divisible by the given range
        if not number % i:
            print("is Not prime")
            return
    print("Is prime")





if __name__ == "__main__":

    number = int(input("Enter a Number"))

    checkPrime(number)