import random

GAME_MODE = 0


def theGame(numberOfGuesses, theNumberToGuess):
    while not numberOfGuesses == 0:
        try:
            userGuess = int(input("Guess The number"))

            if theNumberToGuess > userGuess:
                print(f"To Low number of Guesses left {numberOfGuesses - 1}")
                numberOfGuesses -= 1
            elif theNumberToGuess < userGuess:
                print(f"To High number of Guesses left {numberOfGuesses - 1}")
                numberOfGuesses -= 1
            else:
                print(f"Good the Number is {userGuess} == {theNumberToGuess}")
                break

        except ValueError:
            print("Wrong Datatype")
            print(ValueError)
            continue


def guessNumber():
    global GAME_MODE

    theNumberToGuess = int(random.random() * 101) + 1

    if GAME_MODE:
        print("You Selected Hard mode")
        theGame(5, theNumberToGuess)
    else:
        print("Easy Mode selected")
        theGame(10, theNumberToGuess)


def startGame():
    global GAME_MODE

    # checks for valid input
    while True:
        try:
            value = int(input("Press 0 For easy 1 for hard"))

            # senate check
            if value < 0:
                print("Invalid input")
                continue
            elif value >= 1:
                GAME_MODE = 1
                guessNumber()
                break
            else:
                GAME_MODE = 0
                guessNumber()
                break
        except ValueError:
            print("Invalid DataType")
            continue


if __name__ == "__main__":
    startGame()

    print(GAME_MODE)
    print("main call")
