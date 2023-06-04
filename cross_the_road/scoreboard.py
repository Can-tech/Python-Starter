from turtle import Turtle
FONT = ("Courier", 20, "normal")


class Scoreboard(Turtle):
    def __init__(self):
        super().__init__()
        self.score=0
    def increase_score(self):
        self.score += 1
    def update_score(self):
        self.hideturtle()
        self.penup()
        self.clear()
        self.color("black")
        self.goto(-225,260)
        self.write(f"SCORE: {self.score}", align="center", font=FONT)
    def game_over(self):
        self.goto(0,0)
        self.write(f"GAME OVER", align="center", font=FONT)
