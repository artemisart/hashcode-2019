#!/usr/bin/env python3

from utils import *

from milesial_vert_matcher import run


class Photo:
    def __init__(self, vertical, tags, id):
        self.vertical = vertical
        self.tags = tags
        self.id = id

    def __repr__(self):
        o = 'H'
        if self.vertical:
            o = 'V'
        return f'({o}, id:{self.id}, ntags:{len(self.tags)}, tags:{self.tags})'


def parse_photo(line, id):
    h, _, *tags = line.split()
    return Photo(h == 'V', set(tags), id)


def main():
    photo_count = int(input())
    photos = [parse_photo(input(), i) for i in range(photo_count)]
    all_tags = set(tag for p in photos for tag in p.tags)
    run(photos)
    # err('unique tags', len(all_tags))


if __name__ == '__main__':
    main()
