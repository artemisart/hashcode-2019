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
    max_ingredients = max_cells - min_ingredients
    pizza = [list(input()) for _ in range(rows)]

    # err(pizza[0][:10], '...')
    pizza = np.uint8(np.array(pizza) == 'M')
    err(pizza)

    rects = get_rects(min_ingredients, max_cells)
    err('possible_rects', rects)

    all_rects = []
    for row in range(rows):
        for col in range(columns):
            for rect in rects:
                r_span, c_span = rect
                r_end = row + r_span
                c_end = col + c_span
                if r_end > rows or c_end > columns:
                    continue
                mushrooms = pizza[row:r_end, col:c_end].sum()
                if min_ingredients <= mushrooms <= max_ingredients:
                    all_rects.append((row, col, r_end, c_end))
    err('len all_rects', len(all_rects))
    err('all_rects', all_rects)

    for rect in all_rects:
        print(rect)
        row, col, r_end, c_end = rect
        print(pizza[row:r_end, col:c_end])


if __name__ == '__main__':
    main()
