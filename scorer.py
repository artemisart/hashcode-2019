#!/usr/bin/env python3

from utils import *


def main():
    ds_file, sub_file = sys.argv[1:]
    ds = open(ds_file)
    sub = open(sub_file)

    photo_count = int(ds.readline())
    photos = [parse_photo(ds.readline(), id) for id in range(photo_count)]
    all_tags = set(tag for p in photos for tag in p.tags)
    err('unique tags', len(all_tags))

    slide_count = int(sub.readline())
    slides = [[int(x) for x in sub.readline().split()] for _ in range(slide_count)]

    already_used = [False for _ in photos]
    for slide in slides:
        if len(slide) == 2:
            a, b = slide
            assert (
                photos[a].vertical and photos[b].vertical
            ), f"{slide} should have vertical photos"
            for p in slide:
                assert already_used[p] == False, f"{p} is already used"
                already_used[p] = True
        elif len(slide) == 1:
            a = slide[0]
            assert photos[a].vertical == False, f"{slide} should have horizontal photo"
            assert already_used[a] == False, f"{a} is already used"
            already_used[a] = True

    score = 0
    for a, b in zip(slides, slides[1:]):
        score += calc_score(photos, a, b)
    err('score', score)
    print(score)


if __name__ == "__main__":
    main()
