#!/usr/bin/env python

import numpy as np

from utils import *
from milesial_rectsplitter import rectsplitter


def main():
    rows, columns, min_ingredients, max_cells = ints()
    pizza = [list(input()) for _ in range(rows)]
    pizza_nd = np.array(pizza)
    pizza_nd[pizza_nd == 'T'] = 0
    pizza_nd[pizza_nd == 'M'] = 1
    pizza_nd = pizza_nd.astype(np.int8)
    err(pizza_nd)
    rectsplitter(pizza_nd, min_ingredients, max_cells)


if __name__ == '__main__':
    main()
