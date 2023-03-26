# main game file. In this code we need to guess the maximum number of states and uts
#

import turtle
import pandas as pd

screen = turtle.Screen()
screen.title("Indian States guess game")

image = 'blank_india_map.gif'
screen.addshape(image)
turtle.shape(image)
turtle.setup(width=700,height=650,startx=None,starty=5)

df = pd.read_csv('state_names.csv')
guessed_set = []
t = turtle.Turtle()
t.penup()
t.hideturtle()

score = 0

while score < 36:
    answer_state = screen.textinput(title=f'{score}/36 Guess the States',prompt="Enter the State or UT's next name")
    answer_state = answer_state.title()

    if answer_state == 'Exit':
        break

    for state in df.states:
        if answer_state in guessed_set:
            break
        elif answer_state == state:
            score += 1
            guessed_set.append(answer_state)
            x = df[df.states == answer_state].x
            y = df[df.states == answer_state].y
            t.goto(x.item(),y.item())
            t.write(answer_state,align='center')

for state in df.states:
    if state not in guessed_set:
        t.speed(7)
        t.color('red')
        x = df[df.states == state].x
        y = df[df.states == state].y
        t.goto(x.item(),y.item())
        t.write(state,align='center')

print(f'Your score is {score}/50')

turtle.mainloop()