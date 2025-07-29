from turtle import Turtle
ALIGN = "center"
FONT = ("Courier", 50, "normal")
L_POSITION = -50, 220
R_POSITION = 50 , 220

class ScoreBoard(Turtle):

        def __init__(self):
            super().__init__()
            self.color("white")
            self.penup()
            self.hideturtle()
            self.l_score = 0
            self.r_score = 0
            self.update_scoreboard()

        def update_scoreboard(self):
            self.clear()
            self.goto(L_POSITION)
            self.write(self.l_score, align=ALIGN, font=FONT)
            self.goto(R_POSITION)
            self.write(self.r_score, align=ALIGN, font=FONT)


        def l_point(self):
            self.l_score += 1
            self.update_scoreboard()

        def r_point(self):
            self.r_score += 1
            self.update_scoreboard()
