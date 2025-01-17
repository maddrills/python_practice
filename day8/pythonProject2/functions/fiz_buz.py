def fizz_buzz(number : int) -> str:
    if number % 15 == 0:
        return "fizz buzz"
    elif number % 3 == 0:
        return "fizz"
    elif number % 5 == 0:
        return "buzz"
    else:
        return str(number)


for i in range(1, 101):
    print("{0} -> {1}".format(i, fizz_buzz(i)))



def seq_packer(*packer: str) -> None:
    """
    receives a series of characters and makes it into a tuple
    eg:
    ('h', 'e', 's', 'o', 'y', 'a', 'm')
    h
    e
    s
    o
    y
    a
    m
    :param packer:
    :return:
    """
    print(packer)

    for i in packer:
        print(i)



seq_packer("h","e","s","o","y","a","m")


def var_args(num, *nums, k = 0, **obj):
    print(num)
    print(nums)
    print(k)
    print(obj)



var_args(1, 5,4,3,2,1, k =9, key1 = 81, key2 = 80)