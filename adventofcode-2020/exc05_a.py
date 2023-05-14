#!/usr/bin/env python3
# -*- coding: utf-8 -*-

from collections import defaultdict
from functools import lru_cache
from math import floor, ceil

fn = "exc5_input.txt"
rows = list( open(fn).read().strip().split("\n") )

hSID = 0
for row in rows:
    y = [0,127]
    x = [0,7]
    for c in row:
        if c == "F":
            y[1] = y[1] - ceil((y[1]-y[0])/2)
        elif c == "B":
            y[0] = y[0] + ceil((y[1]-y[0])/2)
        elif c == "L":
            x[1] = x[1] - ceil((x[1]-x[0])/2)
        elif c == "R":
            x[0] = x[0] + ceil((x[1]-x[0])/2)

    SID = (y[0]*8) + x[0]
    if SID > hSID:
        hSID = SID
print(hSID)
