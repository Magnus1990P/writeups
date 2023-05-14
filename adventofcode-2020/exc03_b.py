#!/usr/bin/env python3
# -*- coding: utf-8 -*-

from collections import defaultdict
from functools import lru_cache
import sys

fn = "exc3_input.txt"
chart = list( open(fn).read().strip().split("\n") )

def trav(chart, loc, mov):
    tc = 0
    while loc[0] < height:
        y,x = loc
        if chart[y][x] == "#":
            tc += 1
        loc[0] += mov[0]
        loc[1] =  (x + mov[1]) % width
    return tc

height = len(chart)
width  = len(chart[0])

tc  = trav(chart, [0,0], [1,3])
tc *= trav(chart, [0,0], [1,1])
tc *= trav(chart, [0,0], [1,5])
tc *= trav(chart, [0,0], [1,7])
tc *= trav(chart, [0,0], [2,1])

print( tc )
