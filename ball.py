from turtle import Turtle
<<<<<<< HEAD
=======
START_SPEED = 0.15
INCREASE_SPEED = 1.095
SPEED_LIMIT = 0.40
>>>>>>> 06b216a (Add Decoration File. Add ball speed limit. Add paddle border limit.)

class Ball(Turtle):
    def __init__(self):
        super().__init__()
        self.shape("circle")
        self.color("white")
        self.penup()
<<<<<<< HEAD
        self.x_move = 0.1
        self.y_move = 0.1
=======
        self.x_move = START_SPEED
        self.y_move = START_SPEED
>>>>>>> 06b216a (Add Decoration File. Add ball speed limit. Add paddle border limit.)

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
<<<<<<< HEAD
        self.x_move = 0.1
        self.y_move = 0.1
        self.bounce_x()

    def increase_ball_speed(self):
        self.x_move *= 1.1
        self.y_move *= 1.1
=======
        self.x_move = START_SPEED
        self.y_move = START_SPEED
        self.bounce_x()

    def increase_ball_speed(self):
        if abs(self.x_move) < SPEED_LIMIT:
            self.x_move *= INCREASE_SPEED
            self.y_move *= INCREASE_SPEED
        print(f"Speed is = {abs(self.x_move):.2f}")
>>>>>>> 06b216a (Add Decoration File. Add ball speed limit. Add paddle border limit.)
