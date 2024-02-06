from turtle import Turtle
TURTLE_SHAPE = "square"

BORDER_COLOR = "white"
GRID_COLOR = "grey"
TOP_LEFT = "top_left"
TOP_RIGHT = "top_right"
BOTTOM_RIGHT = "bottom_right"
BOTTOM_LEFT = "bottom_left"
BORDER_WIDTH = 4
DEFAULT_COLOR = "black"
BACKGROUND = "white"


class Board:
    def __init__(self, width, height, pos, block_size, spacer):
        y = pos[1]
        self.segments = ["_"]*20
        for column in range(height):
            x = pos[0]
            cells = []
            for row in range(width):
                new_segment = Turtle()
                new_segment.penup()
                new_segment.shape(TURTLE_SHAPE)
                new_segment.color(DEFAULT_COLOR)
                new_segment.goto(x, y)
                x += block_size + spacer
                cells.append(new_segment)
            y += block_size + spacer
            self.segments[column] = cells

        # self.block_size = block_size
        # self.width = width
        # self.height = height
        # self.width_px = width * block_size
        # self.height_px = height * block_size
        # self.pos = pos
        # self.corners = self.calculate_corner_pos()
        # x = pos[0] + (BORDER_WIDTH * 2) + 3 + ((self.width/2) * 20)
        # y = pos[1] - (BORDER_WIDTH * 2) - 3
        # self.tetrimino_starting_pos = (x, y)
        # self.draw_board()



    # def calculate_corner_pos(self):
    #     top_left = self.pos
    #     top_right = (self.pos[0] + self.width_px, self.pos[1])
    #     bottom_right = (self.pos[0] + self.width_px, self.pos[1] - self.height_px)
    #     bottom_left = (self.pos[0], self.pos[1] - self.height_px)
    #     return {TOP_LEFT: top_left, TOP_RIGHT: top_right, BOTTOM_RIGHT: bottom_right, BOTTOM_LEFT:bottom_left}
    #
    # def draw_board(self):
    #     turtle = Turtle()
    #     self.draw_border(turtle)
    #     # self.draw_grid(turtle)
    #     turtle.hideturtle()
    #
    # def draw_border(self, turtle):
    #     turtle.penup()
    #     turtle.goto(self.corners[TOP_LEFT])
    #     turtle.pencolor(BORDER_COLOR)
    #     turtle.pensize(BORDER_WIDTH)
    #     turtle.pendown()
    #     for pos in self.corners.values():
    #         turtle.goto(pos)
    #     turtle.goto(self.corners[TOP_LEFT])
    #
    # def draw_grid(self, turtle):
    #     turtle.pencolor(GRID_COLOR)
    #     turtle.pensize(2)
    #     for i in range(self.width):
    #         turtle.penup()
    #         x = self.corners[TOP_LEFT][0] + (i * self.block_size) + BORDER_WIDTH
    #         turtle.goto(x, self.corners[TOP_LEFT][1])
    #         turtle.pendown()
    #         turtle.goto(x, self.corners[BOTTOM_LEFT][1])
    #     for i in range(self.height):
    #         turtle.penup()
    #         y = self.corners[BOTTOM_LEFT][1] + (i * self.block_size) + BORDER_WIDTH
    #         turtle.goto(self.corners[BOTTOM_LEFT][0], y)
    #         turtle.pendown()
    #         turtle.goto(self.corners[BOTTOM_RIGHT][0], y)