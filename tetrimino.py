from turtle import Turtle
from random import choice

import shape_data
from shape_data import shapes

TURTLE_SHAPE = "square"




class Tetrimino:

    def __init__(self, pos, shape):
        self.segments = []
        if shape == "random":
            random_key = choice(list(shapes.keys()))
            self.shape = shapes[random_key]
        else:
            self.shape = shapes[shape]

        self.create_tetrimino(self.shape, pos)


    def create_tetrimino(self, detail, pos):
        color = detail["color"]
        for offset in detail["segment_offsets"]:
            x = (offset[0] * (shape_data.TURTLE_SIZE + shape_data.SPACE)) + pos[0]
            y = (offset[1] * (shape_data.TURTLE_SIZE + shape_data.SPACE)) + pos[1]
            segment = self.create_seqment(color, (x, y))
            self.segments.append(segment)

    def create_seqment(self, color, pos):
        new_segment = Turtle()
        new_segment.penup()
        new_segment.shape(TURTLE_SHAPE)
        new_segment.color(color)
        new_segment.goto(pos[0], pos[1])
        new_segment.shapesize(0.9, 0.9)
        return new_segment

    def move_left(self):
        for segment in self.segments:
            new_x = segment.xcor() - 20
            segment.goto(new_x, segment.ycor())

    def move_right(self):
        for segment in self.segments:
            new_x = segment.xcor() + 20
            segment.goto(new_x, segment.ycor())

    def move_down(self):
        for segment in self.segments:
            new_y = segment.ycor() - 20
            segment.goto(segment.xcor(), new_y)