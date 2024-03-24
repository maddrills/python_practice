from prettytable import *

# created a new object from pretty module
table = PrettyTable()

# using the abject methods
table.add_column("Pokemon Name", ["Pikachu", "Squirtle", "Charmander"])
table.add_column("Power", ["5", "6", "10"])

# manipulate the properties or attributes
# makes it left align
table.align = "l"

print(table)