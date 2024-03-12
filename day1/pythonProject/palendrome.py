
def revers(string):
    stringBuilder = ""
    for letter in reversed(string):
        stringBuilder +=letter
    return stringBuilder


print(revers("hello") == "hello")
print(revers("abba") == "abba")


# exchange number without temp

a = input()
b = input()


a = int(a) + int(b)
b = int(a) - int(b)
a = a - b

a = str(a)
b = str(b)

print("a: " + a)
print("b: " + b)


print(len("hello"))