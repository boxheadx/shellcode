#!/bin/python3

import sys

def get_bytes(inpt, dword=4):
        bytes = [hex(ord(c)) for c in inpt]
        print(f"Bytes: {bytes}")
        bytes.reverse()
        cleaned_bytes = [byte[2:] for byte in bytes]
        substringbytes = []
        for i in range(int(len(inpt) / dword)):
                substringbytes.append(''.join(cleaned_bytes)[2*i*dword:2*(i+1)*dword])

        finalle = [f'0x{sub}' for sub in substringbytes]
        print(f"Little endian: {finalle}")

if(len(sys.argv) < 2):
    print("Usage: ./getbytes.py examplestring")
    exit(1)

get_bytes(sys.argv[1])
