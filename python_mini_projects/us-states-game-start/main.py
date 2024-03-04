from turtle import Turtle, Screen
import time
import pandas as pd

screen = Screen()

screen.bgpic('blank_states_img.gif')
screen.setup(800, 600)

is_game_on = True

# data
states_data = pd.read_csv('50_states.csv')

guess_states = []
while is_game_on:
    answer_input = screen.textinput(title=f'{len(guess_states)}/50', prompt='enter state').capitalize()
    state = states_data[states_data['state'] == input]
    if answer_input=='Exit':
        break
    elif len(state) > 0 and input not in guess_states:
        guess_states.append(input)
        turtle = Turtle()
        turtle.hideturtle()
        turtle.penup()
        turtle.goto(int(state.x), int(state.y))
        turtle.write(answer_input, align='center', font=('Courier', 14, 'normal'))
        turtle.dot(5, 'black')

screen.mainloop()
