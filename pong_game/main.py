from turtle import Turtle,Screen
from paddle import Paddle;
from ball import Ball
from scoreboard import Scoreboard;

screen = Screen()
screen.bgcolor("black")
screen.setup(width=800, height=600)
screen.title("PONG")
screen.tracer(0)
r_paddle=Paddle((350,0))
l_paddle=Paddle((-350,0))
screen.tracer(1)
ball=Ball()
scoreboard=Scoreboard()

screen.listen()
screen.onkey(r_paddle.go_up,"Up")
screen.onkey(r_paddle.go_down,"Down")
screen.onkey(l_paddle.go_up,"w")
screen.onkey(l_paddle.go_down,"s")

game_is_on=True
while game_is_on:
    ball.start_move()

    #Detect collision with wall
    if ball.ycor() > 280 or ball.ycor() < -280:
        ball.bounce_y()
    #Detect colision with r_paddle
    if ball.distance(r_paddle) < 60 and ball.xcor() > 330 or ball.distance(l_paddle) < 60 and ball.xcor() < -330:
        ball.bounce_x()
    if(ball.xcor() > 400):
        screen.tracer(0)
        scoreboard.l_point()
        ball.reset_position()
        screen.tracer(1)
    if(ball.xcor() < -400):
        screen.tracer(0)
        scoreboard.r_point()
        ball.reset_position()
        screen.tracer(1)

    



screen.exitonclick()

