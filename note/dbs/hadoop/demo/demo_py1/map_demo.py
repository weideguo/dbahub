#!/bin/env python
import sys

for line in sys.stdin:
    val = line .strip()
    year,temp = val[0:4], val[5:7]
    if year >="2000":
        print("%s\t%s" % (year,temp))

