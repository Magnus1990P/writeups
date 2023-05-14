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


check = "shiny gold"
result = []
tmp = [check]

while tmp:
    key = tmp.pop()
    if key not in result:
        result.append(key)
    else:
        continue
    for ikey in dataset.keys():
        if key in dataset[ikey].keys():
            if ikey not in tmp and ikey not in result:
                tmp.append( ikey )

print( len( result )-1 )
