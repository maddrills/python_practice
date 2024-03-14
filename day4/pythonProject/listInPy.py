#list in py like arrays


states = ["one", "two", "three"]
# ['one', 'two', 'three']
print(states)


states.extend(["four","five"])
# ['one', 'two', 'three', 'four', 'five']
print(states)

# if __name__ == "__main__":
#     print(states)


# you can also negative index apparently
# ['one', 'two', 'three', 'four', 'five']
# moves from the back
print(states[-2])