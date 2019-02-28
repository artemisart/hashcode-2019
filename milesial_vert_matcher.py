#!/usr/bin/env python3
import random
from tqdm import tqdm
from utils import *
import sys


def run():
    in_file, out_file = sys.argv[1:]
    sys.stdin = open(in_file)
    sys.stdout = open(out_file, 'w', encoding='utf8')

    photo_count = int(input())
    photos_all = [parse_photo(input(), id) for id in range(photo_count)]

    photos = filter(lambda p: p.vertical, photos_all)
    photos = sorted(photos, key=lambda p: len(p.tags), reverse=True)
    err('Number of verticals : ', len(photos))
    err('Min tags :', len(photos[-1].tags))
    err('Max tags :', len(photos[0].tags))

    slides = []
    v1 = photos.pop(0)
    while len(photos) > 1:
        closest, furthest = get_closest_and_furthest_photo(v1.tags, photos)
        photos.remove(closest)
        photos.remove(furthest)
        slides.append((furthest, v1))
        v1 = closest

    slides.append((photos[0], v1))

    photos_h = filter(lambda p: not p.vertical, photos_all)
    photos_h = sorted(photos_h, key=lambda p: len(p.tags), reverse=True)


    n_slides = len(slides) + len(photos_h)
    print(n_slides)
    for slide in slides:
        print(str(slide[0].id) + ' ' + str(slide[1].id))

    photos_h = filter(lambda p: not p.vertical, photos_all)
    photos_h = sorted(photos_h, key=lambda p: len(p.tags), reverse=True)
    for p in photos_h:
        print(p.id)

    err(n_slides)

def get_closest_and_furthest_photo(tags, photos):
    best_score_so_far = -999
    best_photos_so_far = []

    worst_score_so_far = -999
    worst_photos_so_far = []

    still_checking_best = True
    still_checking_worst = True

    for i, p in enumerate(photos):
        if still_checking_best:
            inter = len(tags.intersection(p.tags))
            if inter > best_score_so_far:
                best_score_so_far = inter
                best_photos_so_far.append(p)
                # err(best_score_so_far)
                if inter == len(tags):  # can't get better
                    still_checking_best = False
                    continue

            if len(p.tags) < best_score_so_far:  # no more hope (because sorted list)
                still_checking_best = False
                continue

        if still_checking_worst:
            diff = len(p.tags.difference(tags))
            if diff > worst_score_so_far:
                worst_score_so_far = diff
                worst_photos_so_far.append(p)

            if len(p.tags) < worst_score_so_far:
                still_checking_worst = False

        if not still_checking_worst and not still_checking_best:
            break

    if best_photos_so_far[-1] == worst_photos_so_far[-1] and len(worst_photos_so_far) > 1:
        return best_photos_so_far[-1], worst_photos_so_far[-2]
    elif best_photos_so_far[-1] == worst_photos_so_far[-1] and len(best_photos_so_far) > 1:
        return best_photos_so_far[-2], worst_photos_so_far[-1]
    elif best_photos_so_far[-1] == worst_photos_so_far[-1]:
        photos.remove(best_photos_so_far[-1])
        worst = random.choice(photos)
        photos.append(best_photos_so_far[-1])
        return best_photos_so_far[-1], worst
    else:
        return best_photos_so_far[-1], worst_photos_so_far[-1]


if __name__ == '__main__':
    run()
