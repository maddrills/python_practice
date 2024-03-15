strHeights = "156 178 165 171 187"

strArrayOfHeights = strHeights.split()




# when using range i is a position
for i in range(0, len(strArrayOfHeights)):
    strArrayOfHeights[i] = int(strArrayOfHeights[i])


print(strArrayOfHeights)

sum = 0
highest = 0


# when in ing an array it iterates over a given each element
for height in strArrayOfHeights:
    print(height)
    sum+= height

    if highest < height:
        highest = height

print(f"\n{sum} and highest value is {highest}")
