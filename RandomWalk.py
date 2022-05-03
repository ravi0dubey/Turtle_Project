
import random
import turtle as t

timmy1 = t.Turtle()
screen = t.Screen()
timmy1.shape("turtle")
timmy1.speed("fastest")
colors = ["blue","red","cyan","green","yellow"]
direction =[0,90,180,270]
timmy1.pensize(5)

#Random Walk
for _ in range(200):
    timmy1.color(random.choice(colors))
    timmy1.forward(20)
    timmy1.setheading(random.choice(direction))

screen.exitonclick()