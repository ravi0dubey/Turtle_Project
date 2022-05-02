
#from turtle import Turtle, Screen
import random
import turtle as t

timmy1 = t.Turtle()
screen = t.Screen()
timmy1.shape("turtle")
#timmy1.color("red")
colors = ["blue","red","cyan","green","yellow"]

#to draw dashed lines
# for i in range(0,10):
#
#     timmy1.forward(50)
#     timmy1.penup()
#     timmy1.forward(50)
#     timmy1.pendown()
#     timmy1.right(90)
# n = 8
# for i in range(32):
#     timmy1.forward(i*8)
#
#     timmy1.right(120)
    #
    # timmy1.forward(100)
    #
    # timmy1.right(120)
    
    #timmy1.forward(100)


def draw_shapes(no_of_sides):
    degree = 360 / no_of_sides
    for _ in range(no_of_sides):
        timmy1.right(degree)
        timmy1.forward(100)

for no_of_sides in range(3, 11):
    timmy1.color(random.choice(colors))
    print(random.choice(colors))
    draw_shapes(no_of_sides)


# for i in range(1, 4):
#     timmy1.right(120)
#     timmy1.forward(100)
#
# for i in range(1, 5):
#     timmy1.right(90)
#     timmy1.forward(100)
#
# for i in range (1,6):
#     timmy1.right(72)
#     timmy1.forward(100)

# timmy1.right(72)
# timmy1.forward(100)
# timmy1.right(72)
# timmy1.forward(100)
# timmy1.right(72)
# timmy1.forward(100)
# timmy1.right(72)
# timmy1.forward(100)

    

screen.exitonclick()