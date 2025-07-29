from turtle import Turtle
START_SPEED = 0.15
INCREASE_SPEED = 1.095
SPEED_LIMIT = 0.40

class Ball(Turtle):
    def __init__(self):
        super().__init__()
        self.shape("circle")
        self.color("white")
        self.penup()
        self.x_move = START_SPEED
        self.y_move = START_SPEED

    def move(self):
        new_x = self.xcor() + self.x_move
        new_y = self.ycor() + self.y_move
        self.goto(new_x, new_y)

    def bounce_y(self):
        self.y_move *= -1

    def bounce_x(self):
        self.increase_ball_speed()
        self.x_move *= -1

    def reset_position(self):
        self.goto(0,0)
        self.x_move = START_SPEED
        self.y_move = START_SPEED
        self.bounce_x()

    def increase_ball_speed(self):
        if abs(self.x_move) < SPEED_LIMIT:
            self.x_move *= INCREASE_SPEED
            self.y_move *= INCREASE_SPEED
        print(f"Speed is = {abs(self.x_move):.2f}")
