<<<<<<< HEAD
=======
import time
>>>>>>> 06b216a (Add Decoration File. Add ball speed limit. Add paddle border limit.)
from turtle import Screen
from paddle import Paddle
from ball import Ball
from score_board import ScoreBoard
<<<<<<< HEAD

screen = Screen()
screen.tracer(0)
=======
from decorations import Decoration,GameName

screen = Screen()
>>>>>>> 06b216a (Add Decoration File. Add ball speed limit. Add paddle border limit.)
screen.bgcolor("black")
screen.setup(width=800, height=600)
screen.title("Pong")

<<<<<<< HEAD
=======
decorations = Decoration()
game_name = GameName()

screen.tracer(0)
>>>>>>> 06b216a (Add Decoration File. Add ball speed limit. Add paddle border limit.)
r_paddle = Paddle(350,0)
l_paddle = Paddle(-350, 0)

ball = Ball()
score_board = ScoreBoard()
<<<<<<< HEAD

screen.listen()
screen.onkey(fun = r_paddle.up, key = "Up")
screen.onkey(fun = r_paddle.down, key = "Down")
screen.onkey(fun = l_paddle.up, key = "w")
screen.onkey(fun = l_paddle.down, key = "s")

=======
screen.update()
time.sleep(1)

screen.listen()
screen.onkeypress(fun = r_paddle.up, key = "Up")
screen.onkeypress(fun = r_paddle.down, key = "Down")
screen.onkeypress(fun = l_paddle.up, key = "w")
screen.onkeypress(fun = l_paddle.down, key = "s")
>>>>>>> 06b216a (Add Decoration File. Add ball speed limit. Add paddle border limit.)

game_is_on = True
while game_is_on:
    screen.update()
    ball.move()

    # Detect Collision with Wall
    if ball.ycor() > 280 or ball.ycor() < -280 :
        ball.bounce_y()

    # Detect Collision with Paddle
<<<<<<< HEAD
    if ball.distance(r_paddle) < 50 and ball.xcor() > 330 or ball.distance(l_paddle) < 50 and ball.xcor() < -330:
=======
    if (ball.distance(r_paddle) < 50 and ball.xcor() > 325
            or ball.distance(l_paddle) < 50 and ball.xcor() < -325):
>>>>>>> 06b216a (Add Decoration File. Add ball speed limit. Add paddle border limit.)
        ball.bounce_x()

    # Detect Right Paddle miss the ball
    if ball.xcor() > 380 :
        ball.reset_position()
        score_board.l_point()

    # Detect Left Paddle miss the ball
    if ball.xcor() < -380:
        ball.reset_position()
        score_board.r_point()

screen.exitonclick()
