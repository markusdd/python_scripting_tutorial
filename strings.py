#!/usr/bin/env python3

string = "This is a wonderful teststring."

multistring = """
This is a multiline string.

It is very conventient to use.
Use it either for documentation or for e.g. templates
you wish to fill later etc. .
"""

# you can split strings into a list like this,
# split() also takes other strings as seperator, whitespace is default
words = string.split()  # this splits on any whitespace (space, tab etc.)
print("Whitespace split: ", words)
lines = multistring.splitlines()  # this splits on newlines (cross-OS safe)
print("Newline split: ", lines)

# now a few more neat string examples
print("_".join(words))  # take the string we split at whitespace and re-join it, but using _

# custom 'grep' filtering with 3 conditions
print("\nNon-empty lines not ending with a '.' and lines that contain 'later':")
for line in lines:
    if (line and not line.endswith('.')) or 'later' in line:
        print(line)

# some number formatting
i = 1289468
f = -34.8482
print(f"i: {i}\ni(hex, padded 0 to 14 digits): {i:014x}")
print(f"f: {f}\nf(2 comma digits): {f:.2f}")
