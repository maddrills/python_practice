# animals = {
#     "lions" : ["scary", "big", "cat"],
#     "elephant" : ["big", "gray", "wrinkled"],
#     "teddy" : ["cuddly","stuffed"],
# }
#
# # shallow copy example
# things = animals.copy()
# # animals["teddy"] = "toy"
# print(things["teddy"])
# print(animals["teddy"])
#
# print()
#
# #  notice how both the arrays have the same change
# things["teddy"][0] = "Teddy bear"
# print(things["teddy"])
# print(animals["teddy"])
# print(id(things["teddy"]))
# print(id(animals["teddy"]))

# deep copy
import copy

animals = {
    "lions" : ["scary", "big", "cat"],
    "elephant" : ["big", "gray", "wrinkled"],
    "teddy" : ["cuddly","stuffed"],
}

# perform a deep copy
things = copy.deepcopy(animals)

print(things["teddy"])
print(animals["teddy"])

print()

#  notice how both the arrays have the same change
things["teddy"][0] = "Teddy bear"
print(things["teddy"])
print(animals["teddy"])
print(id(things["teddy"]))
print(id(animals["teddy"]))


#  o/p
# ['cuddly', 'stuffed']
# ['cuddly', 'stuffed']
#
# ['Teddy bear', 'stuffed']
# ['cuddly', 'stuffed']
