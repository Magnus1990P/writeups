#!/usr/bin/env python3
# -*- coding: utf-8 -*-

from collections import defaultdict
from functools import lru_cache
import sys
import string

fn = "exc9_input.txt"
data = list(map(int, list( open(fn).read().strip().split("\n") )))

pal = 25
last=[-1,-1]
for d in range(pal, len(data)):
    cand = data[d-pal:d]
    found = False
    for i in range(0,len(cand)-1):
        for j in range(i+1,len(cand)):
            if cand[i]+cand[j] == data[d]:
                found = True
                sys.stdout.write("{} = {} + {}\n".format(data[d], data[d-pal+i], data[d-pal+j]))
                last = [d-pal+i, d-pal+j]
    if found is False:
        print("ERR: ", d, data[d])
        for i in range(0,d):
            j = 0
            s = 0
            while s <= data[d]:
                s += data[i+j]
                if s == data[d]:
                    a1=min(data[i:i+j])
                    a2=max(data[i:i+j])
                    print(data[d], d, i, i+j)
                    print(a1+a2, "=", a1, a2 )
                    print(data[i:i+j])
                    break
                else:
                    j += 1
        break