#!/usr/bin/env python3

# results are integers if all operands are integers
print("1+2 = ", 1+2)
print("1-2 = ", 1-2)
print("3*2 = ", 3*2)
print("3%2 = ", 3%2)
print("3**2 = ", 3**2)
print("3/2 = ", 3/2)  # only exception, this always returns a float
print("3//2 = ", 3//2)

# some overloaded + magic
print("Concatenated lists: ", [1,2,3] + [4,5,6])
print("Concatenated strings: ", "Hello " + "there.")
