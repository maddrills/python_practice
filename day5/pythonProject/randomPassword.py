import random

letters = ['a', 'b', 'c', 'd', 'e',
           'f', 'g', 'h', 'i', 'j',
           'k', 'l', 'm', 'n', 'o',
           'p', 'q', 'r', 's', 't',
           'u', 'v', 'w', 'x', 'y',
           'z', 'A', 'B', 'C', 'D',
           'E', 'F', 'G', 'H', 'I',
           'J', 'K', 'L', 'M', 'N',
           'O', 'P', 'Q', 'R', 'S',
           'T', 'U', 'V', 'W', 'X', 'Y', 'Z']

numbers = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']

symbols = ['!', '#', '$', '%', '&', '(', ')', '*', '+']


passwordLen = int(input("Password Length "))
numberOfNumbers = int(input("Numbers "))
specialChar = int(input("symbols "))


lettersLength = len(letters)
numbersLen = len(numbers)
symbolsLen = len(symbols)

password = ""


def randomLetter():
    return int(random.random() * lettersLength)
def randomNumbers():
    return int(random.random() * numbersLen)
def randomSymbols():
    return int(random.random() * symbolsLen)

if(passwordLen and numberOfNumbers and specialChar):
    #do all three opps
    print("3")
elif(passwordLen and numberOfNumbers):
    #do that
    print("2")
    while(1):
        outerRandom = int(random.random() * 2) + 1
        if(passwordLen and outerRandom == 1):
            password += letters[randomLetter()]
            #build password
            passwordLen -= 1
            continue
        if (numberOfNumbers and outerRandom == 2):
            #build numbers
            password += numbers[randomNumbers()]
            numberOfNumbers -= 1
            continue
        break

elif(passwordLen):
    print("1")
    # he just wants letters
    for i in range(0, passwordLen):
        password += letters[randomLetter()]
else:
    print("wrong password select")


print(password)