#!/usr/bin/env python

import numpy as np

from utils import *


def main():
    rows, columns, min_ingredients, max_cells = ints()
    pizza = [input() for _ in range(rows)]

    err(pizza[0][:10], '...')


if __name__ == '__main__':
    main()
