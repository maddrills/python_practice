import random

word_list = ["aardvark", "baboon", "camel"]
rightWords = []
wrongGuess = 0

# stages = ['''
#   +---+
#   |   |
#   O   |
#  /|\  |
#  / \  |
#       |
# =========
# ''', '''
#   +---+
#   |   |
#   O   |
#  /|\  |
#  /    |
#       |
# =========
# ''', '''
#   +---+
#   |   |
#   O   |
#  /|\  |
#       |
#       |
# =========
# ''', '''
#   +---+
#   |   |
#   O   |
#  /|   |
#       |
#       |
# =========''', '''
#   +---+
#   |   |
#   O   |
#   |   |
#       |
#       |
# =========
# ''', '''
#   +---+
#   |   |
#   O   |
#       |
#       |
#       |
# =========
# ''', '''
#   +---+
#   |   |
#       |
#       |
#       |
#       |
# =========
# ''']

def randomWordChooser():
    theNumber = int(random.random() * len(word_list))

    return word_list[theNumber]


def hanger(count):
    print("N")
    # print(stages[count])

def checkIfWordExists(word, letter):

    print(word)
    print(letter)
    global wrongGuess
    finalWord = ""

    wrong = True

    for i in range(len(word)):
        # iterate through word and compare against input
        if word[i] == letter:
            # add the word to the rightWords array
            rightWords.append(letter)
            # if guess is right
            wrong = False
            break

    # when loop is complete but there was no match
    if wrong:
        wrongGuess += 1


    found = False

    # build The String
    for i in range(len(word)):
        for alphabet in rightWords:
            # check each word against the right choices
            if alphabet == word[i]:
                finalWord += alphabet
                found = True
                break
        if not found:
            finalWord += "_"

        #next iteration its back to false
        found = False


    return finalWord



if __name__ == "__main__":
    print("Main call")

    word = randomWordChooser()
    # word = "aardvark"

    while(True):

        letter = input("Guess A Letter")

        finalWord = checkIfWordExists(word, letter)

        if "_" in finalWord:
            print(finalWord)
            print(wrongGuess)
            # hanger(wrongGuess)
            continue
        break




    # print(checkIfWordExists(word, "q"))
    # print(checkIfWordExists(word, "a"))
    # print(checkIfWordExists(word, "d"))
    # print(checkIfWordExists(word, "v"))
    # print(checkIfWordExists(word, "z"))
    #
    # print(rightWords)
    # print(wrongGuess)
    # main call