#!/usr/bin/env python3
# -*- coding: utf-8 -*-

from collections import defaultdict
from functools import lru_cache
import sys

fn = "exc6_input.txt"
groups = list( open(fn).read().strip().split("\n\n") )
for gid in range(0,len(groups)):
    groups[gid] = groups[gid].strip().split("\n")

tot = 0
for group in groups:
    tot += len( "".join( set("".join(group)) ) )

print(tot)
