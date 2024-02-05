from turtle import Screen
from tetrimino import Tetrimino
import time

SCREEN_WIDTH = 600
SCREEN_HEIGHT = 600
SCREEN_COLOR = "black"
SCREEN_TITLE = "My tetris game"

screen = Screen()
screen.setup(SCREEN_WIDTH, SCREEN_HEIGHT)
screen.bgcolor(SCREEN_COLOR)
screen.title(SCREEN_TITLE)
screen.tracer(0)

tetrimino = Tetrimino((100,100), "random")
screen.update()

screen.listen()
def move_left():
    tetrimino.move_left()
    screen.update()

def move_right():
    tetrimino.move_right()
    screen.update()

def move_down():
    tetrimino.move_down()
    screen.update()

def turn_clockwise():
    tetrimino.turn_clockwise()
    screen.update()

def turn_anticlockwise():
    tetrimino.turn_anticlockwise()
    screen.update()

screen.onkey(key="a", fun=move_left)
screen.onkey(key="d", fun=move_right)
screen.onkey(key="s", fun=move_down)
screen.onkey(key="e", fun=turn_clockwise)
screen.onkey(key="q", fun=turn_anticlockwise)


game_running = True
while game_running:
    time.sleep(0.5)
    move_down()

screen.exitonclick()