
# tim = Turtle()
# tim.shape("turtle") 
# tim.color("OliveDrab4")
# screen = Screen()
# screen.exitonclick()

# tim.pen(fillcolor="blue", pencolor="black", pensize=2)
# def drawASquare():
    # for _ in range(4):
    #     for __ in range(10):
    #         tim.forward(5)
    #         tim.penup()
    #         tim.forward(5)
    #         tim.pendown()
    #     tim.right(90)
# colors=["dark orange","firebrick","gold","dark goldenrod", "deep pink", "indigo"]
# tom=Turtle()
# tom.shape("turtle")
# tom.color("gray")

# def drawMultihexan():
#     for i in range(3,10):
#         turnAngle=360/i
#         for j in range(i):
#             tom.color(random.choice(colors));
#             tom.forward(100)
#             tom.right(turnAngle)
# drawMultihexan()

#####
# from turtle import Turtle, Screen, colormode
# import random
# colormode(255)
# tom=Turtle()

# tom.shape("turtle")
# tom.speed(0)
# tom.pensize(10)
# def random_color():
#     r = random.randint(0,255)
#     g = random.randint(0,255)
#     b = random.randint(0,255)
#     return (r,g,b)

# def drawRandomPath():
#     while True:
#         tom.color(random_color())
#         tom.setheading(random.choice([0,90,180,270]))
#         tom.forward(30)
# drawRandomPath()
####
import turtle

tom=turtle.Turtle()
tom.speed(0)
colors = ["blue", "red", "green", "gold"]
def spirograph():
    degree=0
    color_index=0
    while degree<360:
        tom.color(colors[color_index])
        tom.circle(100)
        degree+=5
        color_index=(color_index+1)%len(colors)
        tom.setheading(degree)
spirograph()

turtle.Screen().exitonclick()








