from turtle import Turtle

class Scoreboard(Turtle):
    def __init__(self):
        super().__init__()
        self.l_score = 0
        self.r_score = 0
        self.update_scores()

    def l_scorer(self):
        self.l_score += 1
        self.update_scores()

    def r_scorer(self):
        self.r_score += 1
        self.update_scores()

    def update_scores(self):
        self.clear()
        self.penup()
        self.color("white")
        self.goto(-40, 250)
        self.write(f"{self.l_score}", False, font=("Arial", 30, 'bold'))
        self.goto(40, 250)
        self.write(f"{self.r_score}", False, font=("Arial", 30, 'bold'))
        self.hideturtle()

    def won(self):
        self.penup()
        self.hideturtle()
        self.goto(-100, 0)
        if self.r_score == 10:
            self.write("Right player won, Game is over", move=False, font=("Arial", 30, 'bold'))
        elif self.l_score == 10:
            self.write("Left player won, Game is over", move=False, font=("Arial", 30, 'bold'))



