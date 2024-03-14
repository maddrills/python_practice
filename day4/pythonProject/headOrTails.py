import random



# random from 0 to not including 2
def randomGen():
    return int(random.random() * 2)





if __name__ == "__main__":

    match randomGen():
        case 0:
            print("Heads")
        case 1:
            print("Tails")


    # print(randomGen())