#!/usr/bin/env python3

import sys
from random import shuffle

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

    # slides = [i for i in range(photo_count) if photos[i].vertical == False]
    slides = []
    last_vertical = None
    verticals = []
    for photo in photos:
        if photo.vertical:
            verticals.append(photo.id)
            # if last_vertical is None:
            #     last_vertical = photo
            # else:
            #     slides.append([last_vertical.id, photo.id])
            #     last_vertical = None
        else:
            slides.append([photo.id])

    for first in range(len(verticals) - 1):
        best = verticals[first + 1]
        best_score = len(photos[verticals[first]].tags | photos[best].tags)
        for second in range(first + 2, len(verticals)):
            score = len(photos[verticals[first]].tags | photos[verticals[second]].tags)
            if score > best_score:
                best_score = score
                best = verticals[second]

    new_slides = [slides.pop()]
    current = new_slides[0]
    while slides:
        max_id = 0
        max_score = 0
        for i, x in enumerate(slides):
            score = calc_score(photos, current, x)
            if score > max_score:
                max_score = score
                max_id = i
        new_slides.append(slides.pop(max_id))
    slides = new_slides

    print(len(slides))
    for slide in slides:
        print(*slide)


if __name__ == '__main__':
    main()
