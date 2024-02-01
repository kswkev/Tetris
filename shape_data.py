# https://www.quora.com/What-is-an-algorithm-for-finding-all-the-possible-Tetris-blocks-and-the-generalization-to-figures-composed-of-N-squares

TURTLE_SIZE = 20
SPACE = 2

shapes = {
    "oblock": {
        "color": "yellow",
        "segment_offsets": [(0,0), (1, 0), (0, -1), (1, -1)]
    },
    "iblock": {
        "color": "blue",
        "segment_offsets": [(0,0), (-1, 0), (1, 0), (2, 0)]
    },
    "jblock": {
        "color": "navy",
        "segment_offsets": [(0,0), (-1, 0), (-2, 0), (0, -1)]
    },
    "lblock": {
        "color": "orange",
        "segment_offsets": [(0,0), (1, 0), (2, 0), (0, -1)]
    },
    "sblock": {
        "color": "green",
        "segment_offsets": [(0,0), (1, 0), (0, -1), (-1, -1)]
    },
    "zblock": {
        "color": "red",
        "segment_offsets": [(0,0), (-1, 0), (0, -1), (1, -1)]
    },
    "tblock": {
        "color": "purple",
        "segment_offsets": [(0,0), (-1, 0), (1, 0), (0, -1)]
    },
}