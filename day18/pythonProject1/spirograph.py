import turtle as t
import random

tim = t.Turtle()



screen = t.Screen()
screen.colormode(255)


def random_Picker():
    r = random.randint(0, 255)
    g = random.randint(0, 255)
    b = random.randint(0, 255)

    return (r, g, b)


def drwSpiroGraph(sizeGap):
    for _ in range(int(350 / sizeGap)):
        tim.speed("fastest")
        tim.color(random_Picker())
        tim.circle(100)
        tim.setheading(tim.heading() + sizeGap)
        tim.circle(100)

drwSpiroGraph(5)

screen.exitonclick()