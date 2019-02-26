import sys


def err(*args, **kw):
    """Print to stderr (but `file` can be overwritten in `**kw`)."""
    print(*args, file=sys.stderr, **kw)


def ints():
    return [int(x) for x in input().split()]


def floats():
    return [float(x) for x in input().split()]
