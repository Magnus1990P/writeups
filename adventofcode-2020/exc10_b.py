#!/usr/bin/env python3
# -*- coding: utf-8 -*-

from collections import defaultdict
from functools import lru_cache
import sys
import string

fn = "exc10_input.txt"
data = sorted(list(map(int, list( open(fn).read().strip().split("\n") ))))

jolt_diff = 3
device_max_jolt = data[-1]+3
data = [0] + data + [data[-1]+3]

L = len(data)
solves = [0,]*L

def rec(index):
    global solves
    e = 0
    for c in range(index+1, L):
        d = (data[c]-data[index])

        if d <= jolt_diff:
            e+=1
        else:
            break
    solves[index] = e
    if index+1 < L:
        rec(index+1)
    return


rec(0)
a = solves[0]

print(solves)
for i in solves[1:-1]:
    a = a +  + i

print(a)