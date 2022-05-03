
#from turtle import Turtle, Screen
import random
import turtle as t

timmy1 = t.Turtle()
screen = t.Screen()
timmy1.shape("arrow")
#timmy1.color("red")
colors = ["blue","red","cyan","green","yellow"]
direction =[0,90,180,270]
timmy1.pensize(10)

#Random Walk
for _ in range(200):
    timmy1.color(random.choice(colors))
    timmy1.forward(10)
    timmy1.setheading(random.choice(direction))

screen.exitonclick()


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