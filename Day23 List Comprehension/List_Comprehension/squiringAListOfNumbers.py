numbers = [1, 1, 2, 3, 5, 8, 13, 21, 34, 55]
list_of_strings = "9,0,32,8,2,8,64,29,42,99".split(',')
def doubleTheList():
    newDouble = [toDouble ** 2 for toDouble in numbers]
    print(newDouble)

def filterOutnumbersLessThan8():
    newFilter = [toFilter for toFilter in numbers if toFilter > 8]
    print(newFilter)

def filterOutEvenNumbers():
    #covert the list to number
    numbers = [int(toBeNumber) for toBeNumber in list_of_strings]

    evenNumbers = [toBeEven for toBeEven in numbers if not toBeEven % 2]
    print(evenNumbers)

def convertStringArrayToIntArray(file):
    fileData = file.read().split("\n")
    return [int(intArray) for intArray in fileData]

def commonElements(arr1, arr2):
    # can also ddo this
    # common = set(arr1).intersection(arr2)
    # common = set(arr1).intersection(set(arr2))
    # if you havent casted to int yet do this
    # it finds the common string literal compares it then coverts it into string
    # result = [int(num) for num in list1 if num in list2]

    # is my version od comprehension
    common = [ele1 for ele1 in arr1 if ele1 in arr2]
    print(common)
def getCommonNumbersInFile():
    intFileData1 = []
    intFileData2 = []
    with open("./files/file1.txt", mode="r") as file1:
        intFileData1 = convertStringArrayToIntArray(file1)

    with open("./files/file2.txt", mode="r") as file2:
        intFileData2 = convertStringArrayToIntArray(file2)

    commonElements(intFileData1, intFileData2)


if __name__ == "__main__":
    doubleTheList()
    filterOutnumbersLessThan8()
    filterOutEvenNumbers()
    getCommonNumbersInFile()
    print("Main call")