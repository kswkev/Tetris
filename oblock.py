from turtle import Turtle

TURTLE_SHAPE = "square"
BLOCK_COLOR = "yellow"

class Oblock:

    def __init__(self):
        self.segments = []
        self.create_tetrimino()

    def create_tetrimino(self):
        self.segments.append(self.create_seqment(0, 0))
        self.segments.append(self.create_seqment(20, 0))
        self.segments.append(self.create_seqment(20, 20))
        self.segments.append(self.create_seqment(0, 20))

    def create_seqment(self, x, y):
        new_segment = Turtle()
        new_segment.penup()
        new_segment.shape(TURTLE_SHAPE)
        new_segment.color(BLOCK_COLOR)
        new_segment.goto(x, y)
        return new_segment