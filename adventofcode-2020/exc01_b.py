#!/usr/bin/env python3
# -*- coding: utf-8 -*-

from collections import defaultdict
from functools import lru_cache
import pandas as pd
import sys

fn = "exc1_input.txt"
data = pd.read_csv( fn )

a = 2020
for d1 in data[(data["data"]) <= (a) ]["data"]:
    for d2 in data[(data["data"]) <= (a-d1) ]["data"]:
        for d3 in data[(data["data"]) <= (a-d1-d2) ]["data"]:
            if (d1+d2+d3) == 2020:
                print(d1, d2, d3, (d1*d2*d3))
