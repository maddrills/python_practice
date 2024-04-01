def optionalArgumentMethod1(a, b = 1, c = 5):
    print(a, b, c)

# can also have a range of argument of unknown size
def rangeOfArgs(*args):
    for i in args:
        print(i)

def sumArangeOfArguments(*numbers):
    total = 0
    for num in numbers:
        total += num
    print(total)


if __name__ == "__main__":
    # 3 1 5
    optionalArgumentMethod1(3)
    # 3 8 5
    optionalArgumentMethod1(3, 8)
    # 3 8 10
    optionalArgumentMethod1(3, 8, 10)
    # 3 10 8
    optionalArgumentMethod1(a = 3, c = 8, b = 10)

    # 4
    # 7
    # 90
    # 12
    # 44
    rangeOfArgs(4,7,90,12,44)

    # 146
    sumArangeOfArguments(4,77,55,10)