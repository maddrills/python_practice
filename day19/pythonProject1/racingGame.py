from turtle import Turtle, Screen

tim = Turtle()
screen = Screen()

# resizer
# we are mentioning the parameter name here for readability
screen.setup(width=500, height=400)
user_bet = screen.textinput(title="Make Your Bet", prompt="Which turtle will win the race? Enter a color:")
print(user_bet)




screen.exitonclick()