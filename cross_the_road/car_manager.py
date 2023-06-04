from turtle import Turtle
import random
COLORS = ["red", "orange", "yellow", "green", "blue", "purple"]
STARTING_MOVE_DISTANCE = 5
MOVE_INCREMENT = 10



class CarManager(Turtle):
    car_speed = STARTING_MOVE_DISTANCE
    def __init__(self,position):
        super().__init__()
        self.shape("square")
        self.shapesize(stretch_len=2.5,stretch_wid=1.5)
        self.penup()
        self.color(random.choice(COLORS))
        self.car_speed=CarManager.car_speed 
        self.goto(position)

    @classmethod
    def increase_car_speed(self):
        CarManager.car_speed += MOVE_INCREMENT
    def move_car(self):
        new_x = self.xcor() - self.car_speed
        self.goto(new_x,self.ycor())
    

            

