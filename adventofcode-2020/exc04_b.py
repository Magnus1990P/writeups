#!/usr/bin/env python3
# -*- coding: utf-8 -*-

from collections import defaultdict
from functools import lru_cache
import sys
import string

fn = "exc4_input.txt"
passports = list( open(fn).read().strip().split("\n\n") )

req = ["byr","iyr","eyr","hgt","hcl","ecl","pid"]

def val_fields(l1, req):
    for elem in req:
        if elem not in l1:
            return False
    return True

def oob(val, tl, th):
    if val < tl or val > th: return True
    return False

def validate(pp, req):
    for elem in pp.keys():
        if elem == "byr":
            if oob(int(pp[elem]), 1920, 2002):
                return False
        elif elem == "iyr":
            if oob(int(pp[elem]), 2010, 2020):
                return False
        elif elem == "eyr":
            if oob(int(pp[elem]), 2020, 2030):
                return False
        elif elem == "hgt":
            if pp[elem][-2:] == "in":
                if oob(int(pp[elem][:-2]), 59, 76):
                    return False
            elif pp[elem][-2:] == "cm":
                if oob(int(pp[elem][:-2]), 150, 193):
                    return False
            else:
                return False
        elif elem == "hcl":
            if pp[elem][0] == "#":
                for c in pp[elem][1:]:
                    if c not in "abcdef0123456789":
                        return False
            else:
                return False
        elif elem == "ecl":
            if pp[elem] not in "amb blu brn gry grn hzl oth":
                return False
        elif elem == "pid":
            if len(pp[elem]) != 9 or pp[elem].isdigit()==False:
                return False
    return True


count = 0
for passport in passports:
    passport = passport.replace("\n", " ").split(" ")
    p = {}

    for data in passport:
        k,v = data.strip().split(":")
        p.update({k:v})

    if val_fields(p.keys(), req) and validate(p, req):
        count+=1
print( count )
