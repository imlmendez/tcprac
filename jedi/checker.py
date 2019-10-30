#!/usr/bin/env python

import sys


def load_deck(filename):
    return [int(line.split()[1]) for line in open(filename)]


def is_subseq(x, y):
    return all(c in iter(y) for c in x)


def is_increasing(l):
    return all(l[i] < l[i + 1] for i in range(len(l) - 1))


c = load_deck(sys.argv[1])
a = load_deck(sys.argv[3])
b = load_deck(sys.argv[2])

if len(a) != len(b) or not is_increasing(a) or not is_subseq(a, c):
    sys.exit(-1)
