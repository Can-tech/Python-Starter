import time
from turtle import Screen
import random
from player import Player
from car_manager import CarManager
from scoreboard import Scoreboard

screen = Screen()
screen.setup(width=600, height=600)
screen.tracer(0)
player=Player()
scoreboard=Scoreboard()
scoreboard.update_score()

screen.listen()
screen.onkeypress(player.go_up,"Up")
screen.onkeypress(player.go_down,"Down")

car_positions = list(range(-240, 241, 30))
previous_number=0
def random_position():
    global previous_number
    random_number=random.choice(car_positions)

    if random_number != previous_number:
        previous_number=random_number
    else:
        random_position()
i=1
car_number=4
cars=[]
game_is_on = True
while game_is_on:
    time.sleep(0.1)
    screen.update()
    random_position()
    if i % car_number == 0:
        car = CarManager((300,previous_number))
        cars.append(car)
        i=0
    i+=1

    for car in cars:
        car.move_car()
        if player.distance(car)<25:
            game_is_on=False
            scoreboard.game_over()

        if car.xcor() < -260:
            car.hideturtle()
            cars.remove(car)
            del car
    if (player.ycor()>280):
        car.increase_car_speed()
        player.reset_player()
        scoreboard.increase_score()
        scoreboard.update_score()
        if(car_number>0):
            car_number-=1   
        print(car_number)
    

screen.exitonclick()
