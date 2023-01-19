#!/usr/bin/env python3
from pprint import pprint

# empty dictionary (key-value store, some languages call it a map or hash map)
d = {}
# empty list
l1 = []

# dict keys can basically be anything that is hashable, so even e.g. tuples are allowed
# but it cannot be anything dynamic like a list, another dict or so, these only work as values
# insertion is just done by inventing another key in the []-access syntax
d["a"] = 123
d[(1, "c")] = "value"

# dict keys and values can easily be retrieved using these functions
# they are iterables, but can be flattened into a list like so
print("Printing dict d keys and values as lists: ")
vals = list(d.values())
print("Values: ", vals)
keys = list(d.keys())
print("Keys: ", keys)

# you can also get an iterator over the items, which unpacks into k(eys) and v(alues)
print("Printing dict d from a for loop: ")
for k, v in d.items():
    print(k, ": ", v)
# especially for more complex types or objects like dicts,
# pprint (aka pretty print) provides a more human readable output
print("Pretty-Printing dict d: ")
pprint(d)

# list and other collection variables are pointers, so l2 = l1 copies the reference, but
# points to the same list, so if you change l1 or l2, the other one changes too
l1.append(1)
l2 = l1
l2.append(2)
# both l1 and l2 have changed because they are just differently named pointers to the same list
print("\nList1: ", l1, " List2: ", l2)
# if you really wish to copy the list to make it independent later, do it like so:
l2 = l1.copy()
l2.append(3)
print("List1: ", l1, " List2 (copied before append): ", l2)
