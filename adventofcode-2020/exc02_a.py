#!/usr/bin/env python3
# -*- coding: utf-8 -*-

from collections import defaultdict
from functools import lru_cache
import pandas as pd
import sys

fn = "exc2_input.txt"
values = list( open(fn).read().strip().split("\n") )

count = 0
for l in values:
    rr,v  = l.split(": ")
    rr,c  = rr.split(" ")
    r1,r2 = map(int, rr.split("-"))

    s = v.count(c)
    if s >= r1 and s<=r2:
        count += 1

print( count )
