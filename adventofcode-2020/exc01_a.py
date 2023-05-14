#!/usr/bin/env python3
# -*- coding: utf-8 -*-

from collections import defaultdict
from functools import lru_cache

fn = "exc1_input.txt"
values = list( map( int, open(fn).read().strip().split("\n") ) )

a = 2020
for c in range(0, len(values)):
    try:
        loc = values.index( a-values[c] )
        if loc == c:
            raise Exception('index', 'same index')
        print( c, values[c], loc, values[loc] )
        print( values[c] * values[loc])
        break
    except:
        pass
