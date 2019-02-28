#!/usr/bin/env python3

import sys
from random import shuffle
from itertools import permutations

# import numpy as np

from utils import *


def main():
    in_file, out_file = sys.argv[1:]
    sys.stdin = open(in_file)
    sys.stdout = open(out_file, 'w', encoding='utf8')

    photo_count = int(input())
    photos = [parse_photo(input(), id) for id in range(photo_count)]
    all_tags = set(tag for p in photos for tag in p.tags)
    err('unique tags', len(all_tags))

    # shuffle(photos)
    photos.sort(key=lambda photo: (photo.vertical, -len(photo.tags)))

    # slides = [i for i in range(photo_count) if photos[i].vertical == False]
    slides = []
    last_vertical = None
    for photo in photos:
        if photo.vertical:
            if last_vertical is None:
                last_vertical = photo
            else:
                slides.append([last_vertical.id, photo.id])
                last_vertical = None
        else:
            slides.append([photo.id])

    WINDOW = 5  # shuffle in WINDOW-2
    STEP = 1
    for i in range(0, len(slides) - WINDOW, STEP):
        max_score = 0
        for order in permutations(range(i + 1, i + WINDOW - 1)):
            full = [i, *order, i + WINDOW - 1]
            err('full', full)

    print(len(slides))
    for slide in slides:
        print(*slide)


if __name__ == '__main__':
    main()
