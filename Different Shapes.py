# from turtle import Turtle, Screen
import random
import turtle as t

timmy1 = t.Turtle()
screen = t.Screen()
timmy1.shape("turtle")
# timmy1.color("red")
colors = ["blue", "red", "cyan", "green", "yellow"]



#To draw Triangle, Square, Pentagon, Hexagon etc
def draw_shapes(no_of_sides):
    degree = 360 / no_of_sides
    for _ in range(no_of_sides):
        timmy1.right(degree)
        timmy1.forward(100)

for no_of_sides in range(3, 11):
    timmy1.color(random.choice(colors))
    print(random.choice(colors))
    draw_shapes(no_of_sides)
