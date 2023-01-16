#!/usr/bin/env python3
from pprint import pprint

# empty dictionary (key-value store, some language call it a map or hash map)
d = {}
# empty list
l = []

d["a"] = 123
d[(1, "c")] = "value"

# especially for more complex types or objects like dicts,
# pprint (aka pretty print) provides a more human readable output
pprint(d)
