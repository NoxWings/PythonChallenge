#!/usr/bin/env python
from sys import stdin

text = "".join(line for line in stdin).replace("\n", "")
out = ""

a = ord("a")
z = ord("z")
distance = (z-a) + 1

for c in text:
    o = ord(c)
    if o >= a and o <= z:
        index = (o - a + 2) % distance
        out += chr(a + index)
    else:
        out += c

print(out)
