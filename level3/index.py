#!/usr/bin/env python
from sys import stdin
import re

pattern = r"(?<=[^A-Z][A-Z]{3})[a-z](?=[A-Z]{3}[^A-Z])"
text = "".join(line for line in stdin).replace("\n", "")
found = "".join(m.group(0) for m in re.finditer(pattern, text))
print(found)
