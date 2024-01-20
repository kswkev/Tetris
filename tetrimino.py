from turtle import Turtle
from shape_data import shapes

TURTLE_SHAPE = "square"




class Tetrimino:

    def __init__(self):
        self.segments = []
        self.create_tetrimino(shapes["oblock"], -200, 0)
        self.create_tetrimino(shapes["iblock"], -100, 0)
        self.create_tetrimino(shapes["jblock"], 0, 0)
        self.create_tetrimino(shapes["lblock"], 100, 0)
        self.create_tetrimino(shapes["sblock"], 200, 0)

        self.create_tetrimino(shapes["zblock"], -100, -100)
        self.create_tetrimino(shapes["tblock"], 0, -100)

    def create_tetrimino(self, detail, xpos, ypos):
        color = detail["color"]
        for offset in detail["segment_offsets"]:
            self.segments.append(self.create_seqment(color, offset[0] + xpos, offset[1] + ypos))

    def create_seqment(self, color, x, y):
        new_segment = Turtle()
        new_segment.penup()
        new_segment.shape(TURTLE_SHAPE)
        new_segment.color(color)
        new_segment.goto(x, y)
        return new_segment
