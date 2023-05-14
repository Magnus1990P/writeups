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

    if (v[r1-1] == c or v[r2-1] == c) and (v[r1-1]!=v[r2-1]):
        count += 1

print( count )
