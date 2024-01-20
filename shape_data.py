TURTLE_SIZE = 20
SPACE = 2

shapes = {
    "oblock": {
        "color": "yellow",
        "segment_offsets": [(0,0), (TURTLE_SIZE + SPACE, 0), (0, TURTLE_SIZE + SPACE), (TURTLE_SIZE + SPACE, TURTLE_SIZE + SPACE)]
    },
    "iblock": {
        "color": "blue",
        "segment_offsets": [(0,0), (TURTLE_SIZE + SPACE, 0), (2 * (TURTLE_SIZE + SPACE), 0), (3 * (TURTLE_SIZE + SPACE), 0)]
    },
    "jblock": {
        "color": "navy",
        "segment_offsets": [(0,0), (0, TURTLE_SIZE + SPACE), (TURTLE_SIZE + SPACE, TURTLE_SIZE + SPACE), (2 * (TURTLE_SIZE + SPACE), TURTLE_SIZE + SPACE)]
    },
    "lblock": {
        "color": "orange",
        "segment_offsets": [(0,0), (0, TURTLE_SIZE + SPACE), (-1 * (TURTLE_SIZE + SPACE), TURTLE_SIZE + SPACE), (-2 * (TURTLE_SIZE + SPACE), TURTLE_SIZE + SPACE)]
    },
    "sblock": {
        "color": "green",
        "segment_offsets": [(0,0), (TURTLE_SIZE + SPACE, 0), (TURTLE_SIZE + SPACE, TURTLE_SIZE + SPACE), (2 * (TURTLE_SIZE + SPACE), TURTLE_SIZE + SPACE)]
    },
    "zblock": {
        "color": "red",
        "segment_offsets": [(0,0), (-1 * (TURTLE_SIZE + SPACE), 0), (-1 * (TURTLE_SIZE + SPACE), TURTLE_SIZE + SPACE), (-2 * (TURTLE_SIZE + SPACE), TURTLE_SIZE + SPACE)]
    },
    "tblock": {
        "color": "purple",
        "segment_offsets": [(0,0), (0, TURTLE_SIZE + SPACE), (-1 * (TURTLE_SIZE + SPACE), TURTLE_SIZE + SPACE), (TURTLE_SIZE + SPACE, TURTLE_SIZE + SPACE)]
    },
}