# remember tuples are final
#  the are imputable
toupleData = (1,2,4);


import turtle as t
import random

tim = t.Turtle()

colours = ["CornflowerBlue",
           "DarkOrchid",
           "IndianRed",
           "DeepSkyBlue",
           "LightSeaGreen",
           "wheat",
           "SlateGray",
           "SeaGreen"]

tim.pensize(10)
directions = [0, 90, 180, 270]

screen = t.Screen()
screen.colormode(255)


def random_Picker():
    r = random.randint(0, 255)
    g = random.randint(0, 255)
    b = random.randint(0, 255)

    return (r, g, b)


count = 0
while(True):
    tim.forward(30)
    tim.color(random_Picker())
    # The choice() method returns a randomly selected element from the specified sequence.
    tim.setheading(random.choice(directions))

    if ++count == 200:
        break



screen.exitonclick()