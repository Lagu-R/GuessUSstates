from turtle import Turtle

text= Turtle()
# constants
FONT = ('Arial', 8, 'normal')

class State_names():

    def __init__(self):
        text.hideturtle()
        text.penup()
        text.color("black")
        

    def move(self, x_cor, y_cor, answer):
        text.goto(x=x_cor, y=y_cor)
        text.write(f"{answer}", align="center", font=FONT)
        