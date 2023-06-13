from turtle import Turtle
import os
print(os.getcwd())
ALIGNMENT = "center"
FONT = ("Arial", 20, "normal")

class Scoreboard(Turtle):
    def __init__(self):
        super().__init__()
        self.score=0
        self.high_score=self.get_high_score_data()
        self.color("white")
        self.hideturtle()
        self.penup()
        self.goto(0,270)
        self.update_scoreboard()

    def get_high_score_data(self):
        with open("snake_game/data.txt", "r") as file:
            data = file.read()
            return int(data) if data else 0
    def write_high_score_data(self, score):
        with open("snake_game/data.txt", "w") as file:
            file.write(str(score))

    def update_scoreboard(self):
        self.clear()
        self.write(f"SCORE: {self.score}   HIGH SCORE: {self.high_score}", align=ALIGNMENT, font=FONT)

    def increase_score(self):
        self.score += 1
        self.clear()
        self.update_scoreboard()
    def reset(self):
        if self.score > self.high_score:
            self.write_high_score_data(self.score)
            self.high_score = self.get_high_score_data()
        self.score = 0
        self.update_scoreboard()
    def game_over(self):
        self.goto(0,0)
        self.write(f"Game Over!", align=ALIGNMENT, font=FONT)
