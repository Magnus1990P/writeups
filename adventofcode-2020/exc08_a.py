#!/usr/bin/env python3
# -*- coding: utf-8 -*-

from collections import defaultdict
from functools import lru_cache
import sys
import string

fn = "exc8_input.txt"
code = list( open(fn).read().strip().split("\n") )

accumulator = 0
ops = ["acc", "jmp", "nop"]

for instruction in code:
    opcode,value = instruction.split(" ")
    print(opcode, value)
