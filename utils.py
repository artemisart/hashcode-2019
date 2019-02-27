import sys


def err(*args, **kw):
    """Print to stderr (but `file` can be overwritten in `**kw`)."""
    print(*args, file=sys.stderr, **kw)


def ints():
    return [int(x) for x in input().split()]


def floats():
    return [float(x) for x in input().split()]


def is_valid_ingredients(rectangle, L):
    assert rectangle.max() <= 1
    assert rectangle.min() >= 0
    return rectangle.sum() >= L and (1 - rectangle).sum() >= L


def is_valid_size(rectangle, H):
    assert rectangle.max() <= 1
    assert rectangle.min() >= 0
    return rectangle.size >= H


def is_valid(rectangle, L, H):
    return is_valid_ingredients(rectangle, L) and is_valid_size(rectangle, H)


