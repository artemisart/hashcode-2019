import sys


class Photo:
    __slots__ = [ 'tags', 'vertical', 'id' ]

    def __init__(self, vertical, tags, id):
        self.vertical = vertical
        self.tags = tags
        self.id = id

    def __repr__(self):
        o = 'V' if self.vertical else 'H'
        return f'({o} id:{self.id} ntags:{len(self.tags)} tags:{self.tags})'


def parse_photo(line, id):
    orient, _, *tags = line.split()
    return Photo(orient == 'V', set(tags), id)


def get_tags(photos: [Photo], slide: [int]):
    if len(slide) == 1:
        return photos[slide[0]].tags
    elif len(slide) == 2:
        return photos[slide[0]].tags | photos[slide[1]].tags
    raise ValueError(f"slide != 1 or 2 photos: {slide}")


def calc_score(photos: [Photo], slide_a: [int], slide_b: [int]):
    a_tags = get_tags(photos, slide_a)
    b_tags = get_tags(photos, slide_b)
    common = len(a_tags & b_tags)
    in_a_not_b = len(a_tags - b_tags)
    not_a_in_b = len(b_tags - a_tags)
    return min(common, in_a_not_b, not_a_in_b)


def err(*args, **kw):
    """Print to stderr (but `file` can be overwritten in `**kw`)."""
    print(*args, file=sys.stderr, **kw)


def ints():
    return [int(x) for x in input().split()]


def floats():
    return [float(x) for x in input().split()]
