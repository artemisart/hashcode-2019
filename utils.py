import sys


class Photo:
    def __init__(self, vertical, tags, id):
        self.vertical = vertical
        self.tags = tags
        self.id = id

    def __repr__(self):
        o = 'H' if self.vertical else 'V'
        return f'({o}, id:{self.id}, ntags:{len(self.tags)}, tags:{self.tags})'


def parse_photo(line, id):
    orient, _, *tags = line.split()
    return Photo(orient == 'V', set(tags), id)


def err(*args, **kw):
    """Print to stderr (but `file` can be overwritten in `**kw`)."""
    print(*args, file=sys.stderr, **kw)


def ints():
    return [int(x) for x in input().split()]


def floats():
    return [float(x) for x in input().split()]
