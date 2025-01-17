# choice = "-"  # initialise choice to something invalid
# while choice != "0":
#     # {'1','2','3','4','5'} or list("12345") or set("1,2,3,4,5")
#     if choice in list("12345"):
#         print("You chose {}".format(choice))
#     else:
#         print("Please choose your option from the list below:")
#         print("1:\tLearn Python")
#         print("2:\tLearn Java")
#         print("3:\tGo swimming")
#         print("4:\tHave dinner")
#         print("5:\tGo to bed")
#         print("0:\tExit")
#
#     choice = input()

print(set("12345"))

nums = (1,2,3,4,5)
print(set(nums))

print(set(range(0, 20,2)))

numbers = set()

# while len(numbers) < 4:
#     next_number = int(input("Please enter your next value: "))
#     numbers.add(next_number)
# print(numbers)


data = ["blue","red","blue","green","red","blue","white",]

unique_data = sorted(set(data))
print(unique_data)
# ['blue', 'green', 'red', 'white']

# create a list of unique data dict.fromkeys(data) returns a new set of data over an iterable
unique_data = list(dict.fromkeys(data))
print(unique_data)