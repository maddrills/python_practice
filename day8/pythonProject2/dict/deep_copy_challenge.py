person1 = {
    "name" : "Mathew",
    "age" : 27,
    "student" : True
}

person2_copy = {}


def my_deepcopy(d : dict) -> dict:
    """copy a dictionary, creating copies of the 'list' or 'dict' values

    the function will crash with an AttributeError if the values aren't
    in the list pr dictionary

    :param d: the dictionary to copy:
    :return a copy of `d`, with the values being copies of the original values:
    """
    shallow_copy = {}

    for key, values in d.items():
        shallow_copy[key] = values
    return shallow_copy



person2_copy = my_deepcopy(person1)
person2_copy["age"] = 50

print(person1)
print(person2_copy)

# copy op is this
# {'name': 'Mathew', 'age': 27, 'student': True}
# {'name': 'Mathew', 'age': 50, 'student': True}