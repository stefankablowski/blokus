
class Tile:
    all_tiles = [
        [
            [True]
        ],
        [
            [True, True] 
        ],
        [
            [True, True, True]
        ],
        [
            [True, True, True, True]
        ],
        [
            [True, True, True, True, True]
        ],
        [
            [True, True],
            [True, True]
        ],
        [
            [True, True, False],
            [False, True, True]
        ],
        [
            [True, True],
            [True, False]
        ],
        [
            [True, False, False],
            [True, True, True]
        ],
        [
            [False, False, True, True],
            [True, True, True, False]
        ],
        [
            [True, True, True],
            [False, True, False]
        ],
        [
            [True, True, True, True],
            [False, True, False, False]
        ],
        [
            [False, True, False],
            [True, True, True],
            [False, False, True]
            
        ],
        [
            [True, True, True, True],
            [False, False, False, True]
        ],
        [
            [True, True, True],
            [False, True, False],
            [False, True, False]
        ],
        [
            [True, True, True],
            [True, False, False],
            [True, False, False]
        ],
        [
            [False, True, False],
            [True, True, True],
            [False, True, False]
        ],
        [
            [True, True, True],
            [False, True, True]
        ],
        [
            [True, False, False],
            [True, True, True],
            [False, False, True]
        ],
        [
            [False, True, False],
            [True, True, True],
            [True, False, False]
        ],
        [
            [True, True, True],
            [True, False, True]
        ],
    ]

    def rotate_tile(matrix, rotations):
        rotations = rotations % 4
        for _ in range(rotations):
            matrix = [list(row) for row in zip(*matrix[::-1])]
        return matrix
    
    def mirror_tile(matrix, vertical):
        if vertical:
            return [row[::-1] for row in matrix]
        else:
            return matrix[::-1]

