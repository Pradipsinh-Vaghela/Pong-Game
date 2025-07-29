from turtle import Turtle
import time

class Decoration(Turtle):
    def __init__(self):
        super().__init__()
        self.hideturtle()
        self.speed(5)
        self.border()
        self.center_line()

    def border(self):
        self.penup()
        self.pensize(15)
        self.color("red")
        self.goto(-400, -290)
        self.pendown()
        self.setheading(90)
        self.forward(590)
        self.setheading(0)
        self.color("blue")
        self.forward(793)
        self.setheading(270)
        self.color("red")
        self.forward(593)
        self.setheading(180)
        self.color("blue")
        self.forward(793)

    def center_line(self):
        self.penup()
        self.color("green")
        self.goto(0, 290)
        self.pensize(4)
        self.setheading(270)
        for _ in range(29):
            self.pendown()
            self.forward(10)
            self.penup()
            self.forward(10)

class GameName(Turtle):
    def __init__(self):
        super().__init__()
        self.penup()
        self.color("yellow")
        self.goto(0,0)
        self.write(arg = "PONG GAME", align="center" ,font=("Arial", 30, "normal"))
        self.color("black")
        time.sleep(2)
        self.clear()
