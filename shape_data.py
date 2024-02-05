# https://www.quora.com/What-is-an-algorithm-for-finding-all-the-possible-Tetris-blocks-and-the-generalization-to-figures-composed-of-N-squares

TURTLE_SIZE = 20
SPACE = 2

shapes = {
    "oblock": {
        "color": "yellow",
        "segment_offsets": {0: [(0,0), (1, 0), (1, -1), (0, -1)],
                            1: [(0,0), (0, -1), (-1, -1), (-1, 0)],
                            2: [(0,0), (-1, 0), (-1, 1), (0, 1)],
                            3: [(0,0), (0, 1), (1, 1), (1, 0)]}
    },
    "iblock": {
        "color": "blue",
        "segment_offsets": {0: [(0,0), (1, 0), (2, 0), (-1, 0)],
                            1: [(0,0), (0, -1), (0, -2), (0, 1)],
                            2: [(0,0), (-1, 0), (-2, 0), (1, 0)],
                            3: [(0,0), (0, 1), (0, 2), (0, -1)]}
    },
    "jblock": {
        "color": "navy",
        "segment_offsets": {0: [(0,0), (-1, 0), (-2, 0), (0, -1)],
                            1: [(0,0), (0, 1), (0, 2), (-1, 0)],
                            2: [(0,0), (1, 0), (2, 0), (0, 1)],
                            3: [(0,0), (0, -1), (0, -2), (1, 0)]}
    },
    "lblock": {
        "color": "orange",
        "segment_offsets": {0: [(0,0), (1, 0), (2, 0), (0, -1)],
                            1: [(0,0), (0, -1), (0, -2), (-1, 0)],
                            2: [(0,0), (-1, 0), (-2, 0), (0, 1)],
                            3: [(0,0), (0, 1), (0, 2), (1, 0)]}
    },
    "sblock": {
        "color": "green",
        "segment_offsets": {0: [(0,0), (1, 0), (0, -1), (-1, -1)],
                            1: [(0,0), (0, -1), (-1, 0), (-1, 1)],
                            2: [(0,0), (-1, 0), (0, 1), (1, 1)],
                            3: [(0,0), (0, 1), (1, 0), (1, -1)]}
    },
    "zblock": {
        "color": "red",
        "segment_offsets": {0: [(0,0), (-1, 0), (0, -1), (1, -1)],
                            1: [(0,0), (0, 1), (-1, 0), (-1, -1)],
                            2: [(0,0), (1, 0), (0, 1), (-1, 1)],
                            3: [(0,0), (0, -1), (1, 0), (1, 1)]}
    },
    "tblock": {
        "color": "purple",
        "segment_offsets": {0: [(0,0), (-1, 0), (1, 0), (0, -1)],
                            1: [(0,0), (0, 1), (0, -1), (-1, 0)],
                            2: [(0,0), (1, 0), (-1, 0), (0, 1)],
                            3: [(0,0), (0, -1), (0, 1), (1, 0)]}
    },
}