from turtle import Screen, Turtle
import time
from snake import Snake
from food import Food
from scoreboard import Scoreboard


screen = Screen()
screen.setup(width=600, height=600)
screen.bgcolor("black")
screen.title("Snek")
screen.tracer(0)


snake = Snake()
scoreboard = Scoreboard()
food = Food()

screen.listen()
screen.onkey(snake.up, "Up")
screen.onkey(snake.down, "Down")
screen.onkey(snake.left, "Left")
screen.onkey(snake.right, "Right")
X_POS_MAX = 280
X_POS_MIN = -280
Y_POS_MAX = 280
Y_POS_MIN = -280


game_is_on = True
while game_is_on:
    screen.update()
    time.sleep(0.1)

    snake.move()

    #Detect collision with food
    if snake.head.distance(food) < 15:
        food.refresh()
        snake.extend()
        scoreboard.score_up()
        print(scoreboard.score)

    #Detect collision with wall
    if snake.head.xcor() >= X_POS_MAX or snake.head.xcor() <= X_POS_MIN or snake.head.ycor() >= Y_POS_MAX or snake.head.ycor() <= Y_POS_MIN:
        scoreboard.reset()
        snake.reset()
         # game_is_on = False

        #Detect collision with tail
    for segment in snake.segments[1:]:
        if snake.head.distance(segment) < 10:
            # game_is_on = False
            scoreboard.reset()









screen.exitonclick()

