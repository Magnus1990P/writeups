#!/usr/bin/env python3
# -*- coding: utf-8 -*-

from collections import defaultdict
from functools import lru_cache
import sys

fn = "exc4_input.txt"
passports = list( open(fn).read().strip().split("\n\n") )

req = ["byr","iyr","eyr","hgt","hcl","ecl","pid"]

def all(l1,req):
    for elem in req:
        if elem not in l1:
            return False
    return True

count = 0
for passport in passports:
    passport = passport.replace("\n", " ").split(" ")
    p = {}
    for data in passport:
        k,v = data.strip().split(":")
        p.update({k:v})

    if all(p.keys(), req):
        count += 1
print( count )
