from itertools import permutations
from collections import defaultdict, namedtuple, Counter


# 2-D points using (x, y) tuples
def X(point): return point[0]
def Y(point): return point[1]


def neighbours4(point):
    'Without diagonals'
    x, y = point
    return [(x + 1, y), (x, y + 1), (x - 1, y), (x, y - 1)]


def neighbours8(point):
    'With diagonals'
    x, y = point
    return [(x + 1, y), (x + 1, y + 1), (x, y + 1), (x - 1, y + 1),
            (x - 1, y), (x - 1, y - 1), (x, y - 1), (x + 1, y - 1)]


def manhattan_distance(p, q):
    return (abs(X(p) - X(q)) + abs(Y(p) - Y(q)))
