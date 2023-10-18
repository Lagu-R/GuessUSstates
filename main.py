# import modules PANDAS FOR DATA and TurTle for visual
import pandas
import turtle
from text import State_names
# varibales
text = State_names()
right_answer = 0
# screen optimisation
screen = turtle.Screen()
screen.title("U.S. States Game")
image = "blank_states_img.gif"
screen.addshape(image)
turtle.shape(image)

## data imports from states name and coordinates

state = pandas.read_csv("50_states.csv")

is_game_on = True
while is_game_on:
    # ask user about state
    answer_state = screen.textinput(title=f"{right_answer}/50 States Correct", prompt="What's another state's name?").title()

    if answer_state != "Off":
        for i in state.state:
            if answer_state == i:
                stat_row = state[state["state"] == answer_state]
                x_cor = stat_row.x.to_list()
                y_cor = stat_row.y.to_list()
                text.move(x_cor[0], y_cor[0], answer_state)
                if right_answer != 50:
                    right_answer+=1
                else:
                    is_game_on = False
    else:
        is_game_on = False

# screen will exit on click 
screen.exitonclick()