from turtle import Turtle, Screen
import random
turtle = Turtle()

directions = [0, 90, 180, 270]
colors = ["red","gold"]
turtle.pensize(15)
turtle.speed(0)

for i in range(200):
  turtle.forward(30)
  turtle.right(random.choice(directions))
  turtle.color(random.choice(colors))





screen = Screen()
screen.exitonclick()