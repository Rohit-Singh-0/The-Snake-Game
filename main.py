from turtle import Turtle, Screen
import time
from snake import Snake
from food import Food
from score import ScoreBoard
time_val = 0.1
screen = Screen()
screen.bgcolor('black')
screen.setup(width=600, height=600)
screen.title('My Snake Game')
screen.tracer(0)

snake = Snake()
food = Food()

screen.listen()
scoreboard = ScoreBoard()
screen.onkey(snake.up, 'Up')
screen.onkey(snake.down, 'Down')
screen.onkey(snake.left, 'Left')
screen.onkey(snake.right, 'Right')
game_is_on = True
while game_is_on:
    screen.update()
    time.sleep(time_val)
    snake.move()
    if snake.head.distance(food) < 15:
        food.random_location()
        scoreboard.food_got_eaten()
        snake.extend()
        time_val = time_val/1.05

    if snake.head.xcor() > 290 or snake.head.xcor() < -290 or snake.head.ycor() > 290 or snake.head.ycor() < -290:
        game_is_on = False
        scoreboard.game_over()
    for segment in snake.segments[1:]:
        if snake.head.distance(segment) < 10:
            game_is_on = False
            scoreboard.game_over()

screen.mainloop()
