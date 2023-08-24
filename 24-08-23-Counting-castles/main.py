# https://projecteuler.net/problem=502

import numpy as np
from typing import Optional
from itertools import product
from tqdm import tqdm


class Solver():
    def __init__(self, w: int, h: int, mod: Optional[int] = None):
        self.width = w
        self.height = h
        self.mod = mod
        # self.heights = np.ones(self.width)

        # self.heights = np.array([2,3,5,2,3,1,5,4])

    def count_blocks(self, heights):
        number_of_blocks = 0
        active_blocks = heights[0]
        diffs = np.diff(heights)

        for dd in diffs:
            if dd == 0:
                continue
            elif dd > 0:
                active_blocks += dd
            elif dd < 0:
                number_of_blocks -= dd

        number_of_blocks += heights[-1]

        return number_of_blocks

    def iterate(self):
        base_iter = list(range(1, self.height + 1))
        number_of_castles = 0

        number_of_possible_heights = self.height**self.width

        for height_sample in tqdm(product(*([base_iter] * self.width)), total=number_of_possible_heights):
            if self.count_blocks(height_sample) % 2 == 1:
                continue
            if self.height not in height_sample:
                continue

            number_of_castles += 1

        return number_of_castles


if __name__ == '__main__':
    solver = Solver(6, 7)
    # solver = Solver(13, 10)
    # solver = Solver(10, 13)

    print(solver.iterate())
