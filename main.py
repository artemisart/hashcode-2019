#!/usr/bin/env python

from utils import *


class Photo:
    def __init__(self, vertical, tags, id):
        self.vertical = vertical
        self.tags = tags
        self.id = id

def parse_photo(line, id):
    h, _, *tags = line.split()
    return Photo(h == 'V', set(tags), id)


def main():
    photo_count = int(input())
    photos = [parse_photo(input(), i) for i in range(photo_count)]
    all_tags = set(tag for p in photos for tag in p.tags)
    err('unique tags', len(all_tags))

if __name__ == '__main__':
    main()
