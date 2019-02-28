#!/usr/bin/env python3

from utils import *


class Photo:
    def __init__(self, vertical, tags):
        self.vertical = vertical
        self.tags = tags


def parse_photo(line):
    h, _, *tags = line.split()
    return Photo(h == 'V', set(tags))


def get_tags(photos: [Photo], slide: [int]):
    if len(slide) == 1:
        return photos[slide[0]].tags
    elif len(slide) == 2:
        return photos[slide[0]].tags | photos[slide[1]].tags
    raise ValueError(f"slide != 1 or 2 photos: {slide}")


def main():
    ds_file, sub_file = sys.argv[1:]
    ds = open(ds_file)
    sub = open(sub_file)

    photo_count = int(ds.readline())
    photos = [parse_photo(ds.readline()) for _ in range(photo_count)]
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
        a_tags = get_tags(photos, a)
        b_tags = get_tags(photos, b)
        common = len(a_tags & b_tags)
        in_a_not_b = len(a_tags - b_tags)
        not_a_in_b = len(b_tags - a_tags)
        score += min(common, in_a_not_b, not_a_in_b)
    err('score', score)
    print(score)


if __name__ == "__main__":
    main()
