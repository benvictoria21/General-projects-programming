# -*- coding: utf-8 -*-
"""scan port scanning script

Automatically generated by Colaboratory.

Original file is located at
    https://colab.research.google.com/drive/1735ifxf5-oFhRHw96qsOB2CNtJsl6pBd
"""

import socket

s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
s.settimeout(5)

host = input("Please enter the IP you want to scan: ")
port = int(input("Please enter the port you want to scan: "))


def portScanner(port):
    if s.connect_ex((host, port)):
        print("The port is closed")
    else:
        print("The port is open")

portScanner(port)