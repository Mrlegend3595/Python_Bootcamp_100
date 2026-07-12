from turtle import Turtle

class Scoreboard(Turtle):
    def __init__(self):
        super().__init__()
        self.p1_score = 0
        self.p2_score = 0
        self.penup()
        self.color("green")
        self.hideturtle()
        self.goto(0, 270)
        self.update()

    def update(self):
        self.clear()
        self.write(f"{self.p2_score} : {self.p1_score}",align="center",font=("Arial", 20, "bold"))


    def increase_p1_score(self):
        self.p1_score += 1
        self.update()

    def increase_p2_score(self):
        self.p2_score += 1
        self.update()

    def game_over(self):
        self.goto(0, 0)
        self.write(f"Game Over",align="center",font=("Arial", 20, "bold"))

