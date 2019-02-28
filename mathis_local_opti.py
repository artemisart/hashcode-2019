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

    ITER = 10
    for iter in range(ITER):
        WINDOW = 7  # shuffle in WINDOW-2
        STEP = 1
        for i in range(0, len(slides) - WINDOW, STEP):
            max_score = None
            max_order = None
            for order in permutations(range(i + 1, i + WINDOW - 1)):
                full_order = [i, *order, i + WINDOW - 1]
                score = sum(
                    calc_score(photos, slides[a], slides[b])
                    for a, b in zip(full_order, full_order[1:])
                )
                # err('full', full_order, score)
                if max_score is None:  # first time is in the original order
                    max_score = score
                elif score > max_score:
                    err(f"improved score from {max_score} to {score}")
                    max_score = score
                    max_order = full_order
            if max_order is not None:
                reordered_slides = [slides[i] for i in max_order]
                # err(reordered_slides)
                slides[i : i + WINDOW] = reordered_slides

    print(len(slides))
    for slide in slides:
        print(*slide)


if __name__ == '__main__':
    main()
