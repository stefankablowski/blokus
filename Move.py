# Serves as a container for storing move related attributes
from dataclasses import dataclass, astuple

@dataclass
class Move:
    tile: list[list[bool]]
    position: tuple[int, int]
    mirrored: bool
    rotations: int
    def __init__(self, tile, position, mirrored = False, rotations = 0):
        self.tile = tile
        self.position = position
        self.mirrored = mirrored
        self.rotations = rotations
        
    def __iter__(self):
        yield from astuple(self)