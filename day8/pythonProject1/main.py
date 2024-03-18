import math


def greet():
    print("Hello")
    print("How do you do?")
    print("Im great today, thank you")


def paint_calc(height, width, cover ):

    # cover the area to be painted
    areaToBePainted = height * width

    print(f"{areaToBePainted} area to be painted")

    print(f"{math.ceil(areaToBePainted / cover)} number of paint cans to cover the wall")





if __name__ == "__main__":
    test_h = int(input())  # Height of wall (m)
    test_w = int(input())  # Width of wall (m)
    coverage = 5

    paint_calc(test_h, test_w, coverage)
    greet()