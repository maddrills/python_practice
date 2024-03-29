#TODO: Create a letter using starting_letter.txt 
#for each name in invited_names.txt
#Replace the [name] placeholder with the actual name.
#Save the letters in the folder "ReadyToSend".
    
#Hint1: This method will help you: https://www.w3schools.com/python/ref_file_readlines.asp
    #Hint2: This method will also help you: https://www.w3schools.com/python/ref_string_replace.asp
        #Hint3: THis method will help you: https://www.w3schools.com/python/ref_string_strip.asp

import ctypes
def listOutAllTheNamesInFile():
    with open("./input/names/invited_names.txt", mode="r") as listOfNames:

        for names in listOfNames.read().split("\n"):
            createAnInviteName(names)


def createAnInviteName(name):
    # write will create a file if it does not exist
    with open(f"./Output/ReadyToSend/letter_for_{name}.txt", mode="w") as newFile:

        newFile.write(fileDataToSend(name))

def fileDataToSend(name):
    with open("./input/letters/starting_letter.txt", mode="r") as fileContent:
        content = fileContent.read().split("\n")

        newWord = False
        newString = ""
        # find the [] to add new word in it
        for cont in content[0]:
            if(cont == "["):
                newWord = True
            if(cont == "]"):
                newString += name
                newWord = False
                continue
            if(newWord):
                continue
            newString+= cont

        content[0] = newString

        # fills every array position with a new line
        return "\n".join(content)

if __name__ == "__main__":
    listOutAllTheNamesInFile()
    print("Main call")
