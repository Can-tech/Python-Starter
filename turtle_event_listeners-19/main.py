from turtle import Turtle, Screen

tim=Turtle()
screen=Screen()

def move_forwards():
    tim.forward(40)
def move_backwards():
    tim.backward(40)
def turn_left():
    tim.left(30)
def trun_right():
    tim.right(30)
def clear():
    tim.clear()
    tim.penup()
    tim.home()
    tim.pendown()

screen.listen()
screen.onkey(key="w", fun=move_forwards)
screen.onkey(key="s", fun=move_backwards)
screen.onkey(key="a", fun=turn_left)
screen.onkey(key="d", fun=trun_right)
screen.onkey(key="c", fun=clear)


screen.exitonclick()