#!/usr/bin/env python

import numpy as np

from utils import *


class Photo:
    def __init__(self, vertical, tags):
        self.vertical = vertical
        self.tags = tags


def parse_photo(line):
    h, _, *tags = line.split()
    return Photo(h == 'V', set(tags))


def main():
    photo_count = int(input())
    photos = [parse_photo(input()) for _ in range(photo_count)]
    all_tags = set(tag for p in photos for tag in p.tags)
    err('unique tags', len(all_tags))


if __name__ == '__main__':
    main()
