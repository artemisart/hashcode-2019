#!/usr/bin/env python3

import sys
from random import shuffle

# import numpy as np

from utils import *
from scorer import get_tags


WIDOW_SIZE = 1000

def main():
    in_file, out_file = sys.argv[1:]
    sys.stdin = open(in_file)
    sys.stdout = open(out_file, 'w', encoding='utf8')

    photo_count = int(input())
    photos = [parse_photo(input(), id) for id in range(photo_count)]
    all_tags = set(tag for p in photos for tag in p.tags)
    err('unique tags', len(all_tags))

    horizontals = []
    verticals = []

    # for p in photos:
    #     if p.vertical:
    #         verticals.append(p)
    #     else:
    #         horizontals.append(p)

    photos.sort(key=lambda p: (p.vertical, +len(p.tags)))
    # verticals.sort(key=lambda p: -len(p.tags))
    # horizontals.sort(key=lambda p: -len(p.tags))
    # pair_verts(verticals)

    slides = []
    last_vertical = None
    # for photo in photos:
    # photos2 = verticals + horizontals
    # photos2.sort(key=lambda p: +len(p.tags))

    # for photo in photos2:
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
    window(photos, slides)
    for slide in slides:
        print(*slide)

def pair_verts(photos):
    for i in range(len(photos)-1):
        max_score = -1000000000000000
        best_photo = None
        for j in range(i, min(len(photos), i + WIDOW_SIZE)):
            a_tags = get_tags(photos, [i])
            b_tags = get_tags(photos, [j])
            score = -len(a_tags & b_tags)
            if score > max_score:
                max_score = score
                best_photo = photos[j]
        photos[i+1], photos[j] = photos[j], photos[i+1]

def window(photos, slides):
    for i in range(len(slides)-1):
        slide = slides[i]
        max_score = 0
        best_slide = None
        for j in range(min(len(slides), i + WIDOW_SIZE)):
            score = calc_score(photos, slide, slides[j])
            if score > max_score:
                max_score = score
                best_slide = slides[j]
                break
        slides[i+1], slides[j] = slides[j], slides[i+1]

if __name__ == '__main__':
    main()
