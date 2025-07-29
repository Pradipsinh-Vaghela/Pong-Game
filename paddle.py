from turtle import Turtle

class Paddle(Turtle):
    def __init__(self,x_axis, y_axis):
        super().__init__()
        self.shape("square")
        self.color("white")
        self.shapesize(stretch_wid=5, stretch_len=1)
        self.penup()
        self.goto(x_axis, y_axis)

    def up(self):
<<<<<<< HEAD
        new_y = self.ycor() + 30
        self.goto(self.xcor(), new_y)

    def down(self):
        new_y = self.ycor() - 30
        self.goto(self.xcor(), new_y)
=======
        if self.ycor() < 235:
            new_y = self.ycor() + 15
            self.goto(self.xcor(), new_y)

    def down(self):
        if self.ycor() > -235:
            new_y = self.ycor() - 15
            self.goto(self.xcor(), new_y)
        print(self.ycor())
>>>>>>> 06b216a (Add Decoration File. Add ball speed limit. Add paddle border limit.)
