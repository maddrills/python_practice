def basicFileManagement():
    fileObject = open("firstFile.txt",mode = "r")
    print(fileObject.read())
    fileObject.close()


def newWayOfFileManagement():
    with open("firstFile.txt", mode="r") as fileObject:
        print(fileObject.read())

def writingToAFileInAppendMode():
    with open("firstFile.txt", mode="a") as fileObject:
        fileObject.write("\n Hello here is an append text")


if __name__ == "__main__":
    basicFileManagement()
    writingToAFileInAppendMode()
    newWayOfFileManagement()