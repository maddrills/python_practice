alpha = "a"
alphabets = []

# 97 to 122 lower
# 65 to 90 upper

# creates an array of alphabets
while True:
    alphabets.append(alpha)
    if alpha == "z":
        break
    alpha = chr(ord(alpha) + 1)


def encryption(word ,skip):

    encryptedWordis = ""

    #take the word and split it into an array of alphabets
    for i in range(len(word)):
        letterInt = ord(word[i])

        # because the 91 is not inclusive
        if letterInt in range(65, 91):

            letterIntEncr = letterInt + skip

            # print(letterIntEncr)
            # if there is an overflow
            if(letterIntEncr > 90):
                letterIntEncr  = (letterIntEncr % 90) + 64

            # print("big")
            # print(f"before {chr(letterInt)} after {chr(letterIntEncr)}")
            encryptedWordis += chr(letterIntEncr)

        elif letterInt in range(97, 123):
            letterIntEncr = letterInt + skip

            # print(letterIntEncr)
            # if there is an overflow
            if (letterIntEncr > 122):
                letterIntEncr = (letterIntEncr % 122) + 96

            # print("big")
            # print(f"before {chr(letterInt)} after {chr(letterIntEncr)}")
            # print("small")
            encryptedWordis += chr(letterIntEncr)


    return encryptedWordis



def deCryption(word ,skip):

    deWord = ""

    for i in range(len(word)):
        letterInt = ord(word[i])

        if letterInt in range(65, 91):
            letterIntEncr = letterInt - skip
            #check if letter goes below 65 signifying a rap around
            if letterIntEncr < 65:
                # then take the result minus it with the max range to get the wrap around
                letterIntEncr = 91 - (65 % letterIntEncr)
                #print(chr(letterIntEncr))

            deWord += chr(letterIntEncr)

        elif letterInt in range(97, 123):
            letterIntEncr = letterInt - skip

            #check if letter goes below 65 signifying a rap around
            if letterIntEncr < 97:
                # then take the result minus it with the max range to get the wrap around
                letterIntEncr = 123 - (97 % letterIntEncr)

            deWord += chr(letterIntEncr)

    return deWord



if __name__ == "__main__":
    encryptionResult = encryption("Zerox", 5)

    print(f"encrypted : {encryptionResult}")

    result = deCryption(encryptionResult, 5)

    print(f"de : {result}")

    print(alphabets)





