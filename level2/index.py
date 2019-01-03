#!/usr/bin/env python
from sys import stdin

a = ord("a")
z = ord("z")

passwd = "".join([c for line in stdin for c in line if (ord(c) >= a and ord(c) <= z)])
print(passwd)
