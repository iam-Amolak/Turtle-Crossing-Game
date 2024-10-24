from turtle import Turtle

FONT = ("Courier", 24, "normal")


class Scoreboard(Turtle):
    def __init__(self):
        super().__init__()
        self.color("black")
        self.penup()
        self.hideturtle()
        self.level = 1

    def update_score(self):
        self.clear()
        self.goto(-280, 250)
        self.write(f"LEVEL : {self.level}", align="left", font=("Courier", 24, "normal"))

    def increase_level(self):
        self.level += 1
        self.update_score()

    def game_over(self):
        self.goto(0, 0)
        self.write("! ! GAME OVER ! !", align="center", font=("Courier", 40, "normal"))
        self.goto(-280, 250)
        self.write(f"LEVEL : {self.level}", align="left", font=("Courier", 24, "normal"))