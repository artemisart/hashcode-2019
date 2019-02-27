import numpy as np
from utils import is_valid_ingredients, is_valid_size


def split_rect_in_two(rectangle, L, H, dim=0):
    if dim == 1:
        rectangle = rectangle.T

    for i in range(1, rectangle.shape[0] - 1):
        rect_l = rectangle[:i, :]
        rect_r = rectangle[i:, :]
        if is_valid_ingredients(rect_l, L):
            return i


def rectsplitter(rect, L, H):
    i = split_rect_in_two(rect, L, H)
    print(i)