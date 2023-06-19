#!/usr/bin/env python

from pwn import *
from Crypto.Util.number import bytes_to_long, long_to_bytes
from Crypto.Hash import SHA256, SHA512, MD5
from binascii import hexlify

import sys

HOST = "hash.tghack.no"
PORT = 2001

conn = remote(HOST, PORT)

RUN = True

quest=conn.recvline(timeout=5).rstrip()
print(quest)
quest=conn.recvline(timeout=5).rstrip()
print(quest)
quest=conn.recvline(timeout=5).rstrip()
print(quest)

ALGS = ["SHA256", "SHA512", "MD5", "SHA3256", "SHA3512"]
i = 0
while RUN:
    i += 1
    quest=conn.recvline(timeout=5).rstrip()
    print( quest )
    data = quest.split(":")
    if data[0] == "Answer":
        data[0] = data[1]
        data[1] = data[2]

    algorithm = None
    string = data[1].strip()
    HASH = None
    for alg in ALGS:
        if alg in data[0]:
            algorithm = alg
    if algorithm is None:
        print( data[0] )
        conn.close()
        sys.exit()

    if algorithm == ALGS[0]:
        HASH = SHA256.new()
    elif algorithm == ALGS[1]:
        HASH = SHA512.new()
    elif algorithm == ALGS[2]:
        HASH = MD5.new()
    elif algorithm == ALGS[3]:
        HASH = SHA3_256.new()
    elif algorithm == ALGS[4]:
        HASH = SHA3_512.new()
    
    HASH.update( string )
    HASH = hexlify( HASH.digest() )
    
    print( "Level: {}/1000".format(i))
    print( "\tAlg:  '{}'".format(algorithm))
    print( "\tText: '{}'".format(string))
    print( "\tHash: '{}'".format( HASH ) )

    conn.sendline( HASH )
    
    print("\n-----------------------------------------------------------------------------------\n")

conn.close()