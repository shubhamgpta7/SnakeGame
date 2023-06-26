from turtle import Turtle


class Scoreboard(Turtle):
    def __init__(self):
        super().__init__()
        self.score = 0
        self.color("white")
        self.penup()
        self.goto(0, 260)
        self.write(f"Score: {self.score}", align="center", font=("Arial", 24, "normal"))
        self.hideturtle()

    def increase_score(self):
        self.clear()
        self.score += 1
        self.write(f"Score: {self.score}", align="center", font=("Arial", 24, "normal"))

    def print_score(self):
        print(f"your score is {self.score}")

    def game_over(self):
        self.color("white")
        self.goto(0,0)
        self.write(f"Game Over",  align="center", font=("Arial", 24, "normal"))
