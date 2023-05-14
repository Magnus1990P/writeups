#!/usr/bin/env python3
# -*- coding: utf-8 -*-

from collections import defaultdict
from functools import lru_cache
import sys
import string

fn = "exc8_input.txt"
data = list( open(fn).read().strip().split("\n") )

program = []
for instruction in data:
    opcode,value = instruction.split(" ")
    value = int(value[1:]) if value[0] == "+" else -1*int(value[1:])
    program.append([opcode,value])

ops = ["acc", "jmp", "nop"]

def execute(address, accumulator, exec_log, altered):
    while address < len(program):
        if address in exec_log:
            return False,-1
        else:
            exec_log.append(address)

        if program[address][0] == ops[0]: #acc
            accumulator += program[address][1]
            address += 1

        elif program[address][0] == ops[1]: #jmp
            res,val = execute(address + program[address][1], accumulator, exec_log, False)
            if res == False and altered == False:
                execute(address+1, accumulator, exec_log, True)
            elif res == True:
                return res, val

        elif program[address][0] == ops[2]: #nop
            res,val = execute(address+1, accumulator, exec_log, True)
            if res == False and altered == False:
                execute(address + program[address][1], accumulator, exec_log, False)
            if res == True:
                return res, val

    print("SUCCESS", accumulator)
    return True, accumulator

print( execute(0, 0, [], False) )
