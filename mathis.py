#!/usr/bin/env python3

import sys

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

    print(len(slides))
    for slide in slides:
        print(*slide)


if __name__ == '__main__':
    main()
