# def tryCatchFunction():
#     try:
#         file = open("a_file.txt")
#         a_dictionary = {"key": "value"}
#         print(a_dictionary["randomKey"])
#     except FileNotFoundError:
#         file = open("a_file.txt","w")
#         file.write("Something")
#     except KeyError as error_message:
#         print(f"Key Error {error_message}")
#     else:
#         content = file.read()
#         print(content)
#     finally:
#         file.close()
#         print("file was close.")
#
#
# def div1():
#     bun_price = 2.40
#     money = 15
#
#     count = 0
#
#     # while True:
#
#     #     money -= bun_price
#
#     #     count+=1;
#
#     #     if money < bun_price:
#     #         break
#
#     remainder = money // bun_price
#
#
#     for i in range(0, int(remainder)):
#         count += 1
#
#     print(count)
#
#
# if __name__ == "__main__":
#     # tryCatchFunction()
#     # number = 5
#     # print("My age is " + str(number))
#     # print("main call")
#     #
#     # for i in range(1, 10):
#     #     print("Number is \t" + str(i))
#     div1()

t = ("a", "b", "c")
print(t)

<<<<<<< HEAD
print(t[0])
=======
def rasingException():
    """ rais an exception that throws a new exception """
    raise TypeError("An error Occurred")
>>>>>>> 45420c24385e6d5ea87e417b1e17cafcec340d9d

metallica2 = list(t)
print(metallica2)