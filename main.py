import random
from turtle import Turtle,Screen

timmy = Turtle()


def change_color():
    R = random.random()
    B = random.random()
    G = random.random()

    timmy.color(R, G, B)


i = 0
timmy.speed(1000)
while i < 75:
    change_color()
    radius = 100
    timmy.circle(radius)
    timmy.left(5)
    i += 1


screen = Screen()
screen.exitonclick()