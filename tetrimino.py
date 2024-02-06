from turtle import Turtle
from random import choice

import shape_data
from shape_data import shapes

TURTLE_SHAPE = "square"


class Tetrimino:

    def __init__(self, pos, shape):
        self.segments = []
        self.direction = 0
        self.segment_detail = None
        if shape == "random":
            random_key = choice(list(shapes.keys()))
            self.shape = shapes[random_key]
        else:
            self.shape = shapes[shape]

        self.create_tetrimino(self.shape, pos)

    def create_tetrimino(self, detail, pos):
        color = detail["color"]
        self.segment_detail = detail["segment_offsets"]
        for offset in self.segment_detail[self.direction]:
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

    def redraw(self):
        anchor_x = self.segments[0].xcor()
        anchor_y = self.segments[0].ycor()
        segment_plans = self.segment_detail[self.direction]
        print(anchor_x, anchor_y)
        print(segment_plans)
        for i in range(1,4):
            x = (segment_plans[i][0] * (shape_data.TURTLE_SIZE + shape_data.SPACE)) + anchor_x
            y = (segment_plans[i][1] * (shape_data.TURTLE_SIZE + shape_data.SPACE)) + anchor_y
            self.segments[i].goto(x, y)

    def move_left(self):
        for segment in self.segments:
            new_x = segment.xcor() - 22
            segment.goto(new_x, segment.ycor())


    def move_right(self):
        for segment in self.segments:
            new_x = segment.xcor() + 22
            segment.goto(new_x, segment.ycor())

    def move_down(self):
        for segment in self.segments:
            new_y = segment.ycor() - 22
            segment.goto(segment.xcor(), new_y)

    def turn_clockwise(self):
        self.direction += 1
        if self.direction >= 4:
            self.direction = 0
        self.redraw()

    def turn_anticlockwise(self):
        self.direction -= 1
        if self.direction <= -1:
            self.direction = 3
        self.redraw()