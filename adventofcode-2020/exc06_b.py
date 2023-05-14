#!/usr/bin/env python3
# -*- coding: utf-8 -*-

from collections import defaultdict
from functools import lru_cache
import sys
import string

fn = "exc6_input.txt"
groups = list( open(fn).read().strip().split("\n\n") )
for gid in range(0,len(groups)):
    groups[gid] = groups[gid].strip().split("\n")

tot = 0
for group in groups:
    if len(group) == 1:
        tot += len(group[0])
    else:
        for ans in group[0]:
            exist = True
            for ind in group[1:]:
                if ans not in ind:
                    exist = False
                    break
            if exist:
                tot+=1

print(tot)
