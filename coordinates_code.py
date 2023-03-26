# to point the actual co-ordinate of each state
# this code is used to build the state_names.csv

import turtle
import pandas as pd

screen = turtle.Screen()
screen.title("Indian States guess game")

image = 'blank_india_map.gif'
screen.addshape(image)
turtle.shape(image)
turtle.setup(width=700,height=650,startx=None,starty=5)

def get_mouse_click_coor(x,y):
   print(x,y)
turtle.onscreenclick(get_mouse_click_coor)




turtle.mainloop()