#!/usr/bin/env python3

import sys
from collections import Counter, defaultdict
from itertools import combinations

import networkx as nx

from utils import *


def main():
    if len(sys.argv) >= 2:
        sys.stdin = open(sys.argv[1])
    if len(sys.argv) >= 3:
        sys.stdout = open(sys.argv[2], 'w', encoding='utf-8')

    photo_count = int(sys.stdin.readline())
    photos = [parse_photo(sys.stdin.readline(), id) for id in range(photo_count)]
    all_tags = Counter(tag for p in photos for tag in p.tags)
    err('unique tags', len(all_tags))
    # lines = sys.stdin

    horizontals, verticals = [], []
    for photo in photos:
        (verticals if photo.vertical else horizontals).append(photo)

    v_by_tags = {}
    for v in verticals:
        for tag in v.tags:
            v_by_tags.setdefault(tag, []).append(v)
    gv = nx.Graph()
    for a, b in combinations(verticals, 2):
        c = len(a.tags & b.tags)
        if c == 0:
            gv.add_edge(a, b)
    ordered = nx.dfs_preorder_nodes(gv)
    v_merged = [
        Photo(False, a.tags | b.tags, f'{a.id} f{b.id}')
        for a, b in zip(ordered[::2], ordered[1::2])
    ]

    photos = horizontals + v_merged
    # for slide in slides:
    #     if len(slide) == 1:
    #         photos.append(slide[0])
    #     else:
    #         a, b = slide
    #         photos.append(Photo(False, a.tags | b.tags, f'{a.id} {b.id}'))
    err(photos)

    # def parse_line(line):
    #     orient, _, *tags = line.split()
    #     return orient == 'V', tags

    # photos = [parse_line(line) for line in lines]

    # inverted index
    photos_by_tag: dict = defaultdict(list)
    for p in photos:
        for tag in p.tags:
            if all_tags[tag] > 1:
                photos_by_tag[tag].append(p.id)
    # err(photos_by_tag)

    # graph of connected photos (common tags)
    G = nx.Graph(uv for uvs in photos_by_tag.values() for uv in nx.utils.pairwise(uvs))

    # dfs to discover linked photos
    nodes = list(nx.dfs_preorder_nodes(G))
    print(len(nodes))
    print(*nodes, sep='\n')


if __name__ == "__main__":
    main()
