#!/usr/bin/env python3

from utils import *

from milesial_vert_matcher import run


def main():
    photo_count = int(input())
    photos = [parse_photo(input(), i) for i in range(photo_count)]
    all_tags = set(tag for p in photos for tag in p.tags)
    run(photos)
    err('unique tags', len(all_tags))


if __name__ == '__main__':
    main()
