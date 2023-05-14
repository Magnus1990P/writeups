#!/usr/bin/env python3
# -*- coding: utf-8 -*-

from collections import defaultdict
from functools import lru_cache
import sys
import string

fn = "exc7_input.txt"
data = list( open(fn).read().replace(" bags", "").replace(" bag", "").strip().split("\n") )
dataset = {}
for a in data:
    okey,values = a.split("contain")
    okey=okey.strip()
    values=values.replace(".","").strip()
    content = {}
    for value in values.split(","):
        a = value.strip().split(" ")
        n = a[0].strip()
        skey = " ".join(a[1:]).strip()
        if n.isdigit():
            content.update({skey:int(n)})
    dataset.update({okey:content})

def rec(key, n, i):
    tot = 0
    if len(dataset[key]) == 0:
        return 0
    for skey in dataset[key].keys():
        tot =  tot +  dataset[key][skey] + (dataset[key][skey] * rec(skey, dataset[key][skey], i+1) )
    return tot

okey = "shiny gold"
print( rec(okey, 1, 0) )
