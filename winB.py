import sys
from collections import defaultdict

import networkx as nx

in_file, out_file = sys.argv[1:]
sys.stdin = open(in_file)
sys.stdout = open(out_file, 'w', encoding='utf-8')

sys.stdin.readline()
lines = sys.stdin

# inverted index
photos_by_tag: dict = defaultdict(list)
for id, line in enumerate(lines):
    for tag in line.split()[2:]:
        photos_by_tag[tag].append(id)

# graph of connected photos (common tags)
G = nx.Graph(uv for uv in photos_by_tag.values() if len(uv) == 2)

# dfs to discover linked photos
nodes = list(nx.dfs_preorder_nodes(G))
print(len(nodes))
print(*nodes, sep='\n')
