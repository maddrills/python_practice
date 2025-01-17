# def multiply():
#     """
#     :return: sum of two numbers
#     """
#     return 2 * 3
#
#
# def is_palindrome(string):
#     return string.casefold() == string[::-1].casefold()
#
#
# print(multiply())
#
# def groin(multiplier):
#     print(multiplier())
#
#
# groin(multiply)
#
# print(is_palindrome("Acbca"))
# print(is_palindrome("mathew"))
#
# # palindrome in sentence
# def sentence_palindrome(stringOfWords):
#
#     newWord = ""
#     for i in stringOfWords:
#         if i.isalnum():
#             newWord += i.casefold()
#
#     print(is_palindrome(newWord))
#
#
# sentence_palindrome("Was it a car, or a cat, i saw")
# sentence_palindrome("Do geese see god")
# sentence_palindrome("Desnes not far, Rafton sensed")
#
#
# def sum_eo(n, t):
#     if n < 1 or not t.isalpha() or len(t) > 1: return -1
#
#     validResponse = "oe"
#     if t.casefold() not in validResponse: return -1
#
#     if t.casefold() == "e":
#         print("In e")
#         for i in range(2, n, 2):
#             print(i)
#     else:
#         for i in range(1, n, 2):
#             print(i)
#
#
#
# sum_eo(10, "o")
# sum_eo(10, "e")


def fib_function(limit : int = 0) -> int:
    """
    displays a range of fib numbers till you hit a limit
    :param limit: a `+ve int` number
    :return: nothing
    """
    if 0 <= limit <= 1:
        return limit

    first , second = (0, 1)
    print(first,second,end=" ")
    result = None
    for f in range(0, limit -1):
        result = first + second
        first = second
        second = result
        print(result, end=" ")

fib_function(10)







