# print(ord("A") - 65)
# ord() coverts letter to ascii value

def alphaToPos(alpha):
    alpha = alpha.upper()
    if(alpha >= "A" and alpha <= "C"):
        return ord(alpha) - 65
    else:
        return


tickTack = [
    ["", "", ""],
    ["", "", ""],
    ["X", "", ""]
]

def findTheBox(input):
    input = input.strip()
    args = []
    if(len(input) < 2):
        return "Invalid Input"

    try:
        args.append(int(input[0]) - 1)
        args.append(alphaToPos(input[1]))
    except:
        return "invalid input"
    return args


def tickTackToSearch(args):
    return tickTack[args[0]][args[1]]


print(tickTackToSearch(findTheBox("3a")))