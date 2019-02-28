#!/usr/bin/env python

from utils import *


def main():
    slices_count = int(input())
    slices = [
        ints()  # row_start, column_start, row_end, column_end
        # start and end included
        for _ in range(slices_count)
    ]

    score = sum((r2 - r1 + 1) * (c2 - c1 + 1) for r1, c1, r2, c2 in slices)


if __name__ == "__main__":
    main()
