from oblock import Oblock

TURTLE_SHAPE = "square"
TURTLE_COLOR = "white"
TURTLE_SIZE = 20


class Tetrimino:

    def __init__(self):
        self.segments = []
        block = Oblock()
        self.segments = block.segments
