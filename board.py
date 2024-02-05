from turtle import Turtle

BORDER_COLOR = "white"
GRID_COLOR = "grey"
TOP_LEFT = "top_left"
TOP_RIGHT = "top_right"
BOTTOM_RIGHT = "bottom_right"
BOTTOM_LEFT = "bottom_left"


class Board:
    def __init__(self, width, height, pos, block_size):
        self.block_size = block_size
        self.width = width
        self.height = height
        self.width_px = width * block_size
        self.height_px = height * block_size
        self.pos = pos
        self.corners = self.calculate_corner_pos()
        self.tetrimino_starting_pos = (pos[0] + (self.width_px/2) + (block_size/2), pos[1] - block_size/2)
        self.draw_board()

    def calculate_corner_pos(self):
        top_left = self.pos
        top_right = (self.pos[0] + self.width_px, self.pos[1])
        bottom_right = (self.pos[0] + self.width_px, self.pos[1] - self.height_px)
        bottom_left = (self.pos[0], self.pos[1] - self.height_px)
        return {TOP_LEFT: top_left, TOP_RIGHT: top_right, BOTTOM_RIGHT: bottom_right, BOTTOM_LEFT:bottom_left}

    def draw_board(self):
        turtle = Turtle()
        self.draw_border(turtle)
        # self.draw_grid(turtle)
        turtle.hideturtle()

    def draw_border(self, turtle):
        turtle.penup()
        turtle.goto(self.corners[TOP_LEFT])
        turtle.pencolor(BORDER_COLOR)
        turtle.pensize(4)
        turtle.pendown()
        for pos in self.corners.values():
            turtle.goto(pos)
        turtle.goto(self.corners[TOP_LEFT])

    def draw_grid(self, turtle):
        turtle.pencolor(GRID_COLOR)
        turtle.pensize(2)
        for i in range(self.width):
            turtle.penup()
            x = self.corners[TOP_LEFT][0] + (i * self.block_size)
            turtle.goto(x, self.corners[TOP_LEFT][1])
            turtle.pendown()
            turtle.goto(x, self.corners[BOTTOM_LEFT][1])
        for i in range(self.height):
            turtle.penup()
            y = self.corners[BOTTOM_LEFT][1] + (i * self.block_size) + 2
            turtle.goto(self.corners[BOTTOM_LEFT][0], y)
            turtle.pendown()
            turtle.goto(self.corners[BOTTOM_RIGHT][0], y)