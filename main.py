#!/usr/bin/env python

import numpy as np

from utils import *


def get_rects(min_ingredients, max_cells):
    min_cells = min_ingredients * 2
    rects = []
    for size in range(min_cells, max_cells + 1):
        for rowspan in range(1, size):
            if size % rowspan != 0:
                continue
            colspan = size // rowspan
            rects.append((rowspan, colspan))
    return rects


def main():
    rows, columns, min_ingredients, max_cells = ints()
    pizza = [list(input()) for _ in range(rows)]

    # err(pizza[0][:10], '...')
    pizza = np.uint8(np.array(pizza) == 'M')
    err(pizza)

    rects = get_rects(min_ingredients, max_cells)
    err(rects)


if __name__ == '__main__':
    main()
