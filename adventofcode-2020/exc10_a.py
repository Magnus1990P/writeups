#!/usr/bin/env python3
# -*- coding: utf-8 -*-

from collections import defaultdict
from functools import lru_cache
import sys
import string

fn = "exc10_input.txt"
data = sorted(list(map(int, list( open(fn).read().strip().split("\n") ))))

joltmin = -3
outlet = 0
device_max_jolt = data[-1]+3
diff = [0,0,0]
jolt = outlet
for c in range(0,len(data)):
    diff[ data[c]-jolt-1 ] += 1
    jolt = data[c]
diff[device_max_jolt-data[-1]-1] += 1

print(diff)
print(diff[0]*diff[2])
