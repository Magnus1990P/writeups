#!/usr/bin/env python

from pwn import *
from Crypto.Util.number import bytes_to_long, long_to_bytes
from binascii import hexlify

import sys

HOST = "bytes.tghack.no"
PORT = 2010

conn = remote(HOST, PORT)

RUN = True

i = 0
while RUN:
    i += 1
    quest=conn.recvline(timeout=5).rstrip()
    data=conn.recvline(timeout=5).rstrip()
    
    print("Level: {}/1000".format(i))
    print( "{}".format(quest) )
    for j in range(0,len(data),100):
        print( "\t{}".format(data[j:j+100]) )

    ret = ""
    if quest == "Here's some bytes:":
        print("Converting bytes to number" )
        ret = str( long(data, 16) ).rstrip()

    elif quest == "Here's a number:":
        print("Converting number to bytes")
        ret = long(data)
        ret = long_to_bytes( ret )
        ret = hexlify( str(ret) )

    else:
        print("No match")
        print("'{}'".format(quest))
        RUN = False
        break

    for j in range(0,len(data),100):
        print( "\t{}".format(ret[j:j+100]) )
    
    conn.sendline( ret )
    res = conn.recvline(timeout=5).rstrip()
    
    if( res[-4:] == "Yay!" ):
        print("Correct answer")

    elif res[-5:] == "Nope!":
        print("Wrong answer")
        RUN = False
    
    print("\n\n-----------------------------------\n\n")

    if i == 1000:
        print( res )
        res = conn.recvline(timeout=5).rstrip()
        print( res )
        RUN = False
        

conn.close()
