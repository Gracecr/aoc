from __future__ import annotations

import sys

sys.setrecursionlimit(10000)

import dataclasses
import functools
import inspect
import itertools
import math
import operator
import re
from collections import ChainMap, Counter, defaultdict, deque
from collections.abc import Mapping
from pathlib import Path

import networkx as nx
import numpy as np
from aocd import _impartial_submit
from aocd import get_data as __get_data


def __get_calling_context():
    return next(context for context in inspect.stack() if context.filename != __file__)


def __get_day_and_year():
    calling_context = __get_calling_context()
    path = Path(calling_context.filename)
    day = int(path.stem)
    year = int(path.parent.name)
    return day, year


def get_data() -> str:
    day, year = __get_day_and_year()
    return __get_data(day=day, year=year)


def submit(answer, part=None):
    day, year = __get_day_and_year()
    return _impartial_submit(answer, part=part, day=day, year=year)


num_regex = re.compile(r"-?\d+")


def get_vectors(dim, dist=1, diag=False):
    if diag:
        cart_prod = list(itertools.product(range(-dist, dist + 1), repeat=dim))
        cart_prod.remove((0, 0))
        return np.array(cart_prod)
    return np.concatenate((np.eye(dim, dtype=int), -np.eye(dim, dtype=int)))


def addt(t1, t2):
    assert len(t1) == len(t2)
    return tuple(t1[i] + t2[i] for i in range(len(t1)))


def get_neighbors(pos, vectors, bounds=None):
    neighbors = [
        addt(pos, v) for v in vectors if bounds is None or is_in_bounds(bounds, pos)
    ]
    return [n for n in neighbors if bounds is None or is_in_bounds(bounds, n)]


def get_bounds(data):
    current_dim = data
    bounds = []
    while __is_sequence_like(current_dim):
        # Allow for character values as data
        if isinstance(current_dim, str) and len(current_dim) <= 1:
            break
        bounds.append((0, len(current_dim)))
        current_dim = current_dim[0]
    return bounds


def is_in_bounds(bounds, pos):
    return all(bound[0] <= dim < bound[1] for bound, dim in zip(bounds, pos))


def __is_sequence_like(test_obj):
    # numpy.ndarray does not follow sequence protocol :(, so we do this instead
    # https://stackoverflow.com/a/63180722
    return hasattr(test_obj, "__getitem__") and not isinstance(test_obj, Mapping)
