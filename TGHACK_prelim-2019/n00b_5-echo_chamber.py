#!/usr/bin/env python3

import socket
import time

HOST = "echo.tghack.no"
PORT = 5555

with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
    s.connect((HOST,PORT))
    for i in range(0,60):
        data = None
        data = s.recv(1024)
        print(data)

        s.sendall( data )
        time.sleep(1/10)
            

