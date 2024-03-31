sentence = "Hello My Name Is Mathew"

def sentanceToArray():
    global sentence

    return sentence.split(" ")

def countNumberOfWords(words):

    wordAndCount = {word: len(word) for word in words}
    print(wordAndCount)

    #iterate over a dictonary
    # dictionarySpread = {key: value for (key, value) in wordAndCount.items()}
    dictionarySpread = {key: value for (key, value) in wordAndCount.items() if value > 2}
    print(dictionarySpread)


if __name__ == "__main__":
    print(sentanceToArray())
    countNumberOfWords(sentanceToArray())
    print("Main call");