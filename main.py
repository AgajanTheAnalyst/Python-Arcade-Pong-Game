from turtle import Screen, Turtle
from paddle import Paddle
from ball import Ball
from scoreboard import Scoreboard
import time

screen = Screen()
turtle = Turtle()
scoreboard = Scoreboard()
r_paddle = Paddle(350)
l_paddle = Paddle(-350)
ball = Ball()

screen.bgcolor("black")
screen.setup(width=800, height=600)
screen.title("Pong")
screen.tracer(0)

screen.listen()
screen.onkey(r_paddle.up, "Up")
screen.onkey(r_paddle.down, "Down")
screen.onkey(l_paddle.up, "w")
screen.onkey(l_paddle.down, "s")

game_is_on = True
while game_is_on:
    time.sleep(ball.ball_speed)
    screen.update()
    ball.move()
    #Detect collision with wall
    if ball.ycor() > 280 or ball.ycor() < -280:
        ball.bounce_y()
    #Detect collision with r_paddle
    if ball.distance(r_paddle) < 50 and ball.xcor() > 340 or ball.distance(l_paddle) < 50 and ball.xcor() < -340:
        ball.bounce_x()
    if ball.xcor() > 390:
        ball.reset_position()
        scoreboard.l_scorer()
    if ball.xcor() < -390:
        ball.reset_position()
        scoreboard.r_scorer()
    if scoreboard.l_score == 10 or scoreboard.r_score == 10:
        scoreboard.won()
        game_is_on = False




screen.exitonclick()
