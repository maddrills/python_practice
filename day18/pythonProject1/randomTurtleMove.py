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

tim.forward(30)
# The choice() method returns a randomly selected element from the specified sequence.
tim.setheading(random.choice(directions))

count = 0
while(True):
    tim.forward(30)
    tim.color(random.choice(colours))
    # The choice() method returns a randomly selected element from the specified sequence.
    tim.setheading(random.choice(directions))

    if ++count == 200:
        break


screen = t.Screen()
screen.exitonclick()