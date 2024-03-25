import turtle

tinnyTurtle = turtle.Turtle()

tinnyTurtle.shape("turtle")


# creating a five sided shape
number_of_turns = 4
while(number_of_turns < 20):
    for _ in range(number_of_turns):
        # angle of turn
        angle = 360 / number_of_turns
        # move 100
        tinnyTurtle.forward(100)
        tinnyTurtle.right(angle)
    number_of_turns+=1


screen = turtle.Screen()
screen.exitonclick()