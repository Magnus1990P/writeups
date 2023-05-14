#!/usr/bin/env python

from pwn import *

HOST = "math.tghack.no"
PORT = 10000

conn = remote(HOST, PORT)

RUN = True
i = 0
while RUN:
    i += 1
    quest   = conn.recvline(timeout=5).rstrip()
    data    = conn.recvline(timeout=5).rstrip()
    
    print("Q {}/1000: {}".format(i, data))

    ans     = 0
    math    = data.split(" ")
    sign    = math[1]
    a       = long( math[0], 10 )
    b       = long( math[2], 10 )

    if sign == "*":
        ans = a * b
    elif sign == "/":
        ans = a / b
    elif sign == "+":
        ans = a + b
    elif sign == "-":
        ans = a - b
    else:
        print( math )

    conn.sendline( str(ans) )
    data = conn.recvline(timeout=5).rstrip()
    print("\t{} {} {} = {}".format(a,sign,b, ans))
    print("\t{}".format(data))

    
    if data != "Answer: Yay!":
        RUN = False
    elif i == 1000:
        data = conn.recvline(timeout=5).rstrip()
        print("FLAG:  {}".format(data))
        RUN = False

conn.close()


