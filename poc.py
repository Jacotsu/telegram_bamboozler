#!/usr/bin/env python3
import sys

covfefe_char = "\u200C"

try:
    msg = " ".join(sys.argv[1:])
    print(msg + covfefe_char*(4096-len(msg)))
except:
    pass
