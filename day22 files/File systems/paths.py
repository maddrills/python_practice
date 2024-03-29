def absalutePath():
    with open("C:/Users/mathe/OneDrive/Desktop/firstFile.txt", mode="r") as fileFoundInDeskTop:
        print(fileFoundInDeskTop.read())


# relative paths are in relation to you
# here head and move are parents move up a dir and find ../anyOtherDir/file.txt or ..head/move/down/file.txt

# current directory in move ./move/down/file.txt

if __name__ == "__main__":
    print("Main Exe")
    absalutePath()