# Higher order function and event listeners
from turtle import Turtle, Screen

josh = Turtle()
screen = Screen() #objects




def move_forwards():
  josh.forward(10)
def move_back():
  josh.back(10)
def move_left():
  josh.left(10)
def move_right():
  josh.right(10)


screen.onkey(key="w", fun=move_forwards) #function in a function
screen.onkey(key="a", fun=move_left)
screen.onkey(key="s", fun=move_back)
screen.onkey(key="d", fun=move_right)
screen.listen() #this is the event listener
screen.exitonclick() #this makes the screen not exit right away, only after the click
