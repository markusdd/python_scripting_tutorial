#!/usr/bin/env python3
from pprint import pprint

# enumerate provides a very conventient way to iterate over a collection
# and get a counter variable for free, the start is 0 by default, here we choose 1
letters = ['a', 'b', 'c', 'd']
for i, letter in enumerate(letters, start=1):
    print(f"{i} {letter}")
# len lets you know the size of a collection like lists
print(f"There are {len(letters)} in the letters list.")

# range provides an iterator to easily generate series of numbers
# we use Pythons list comprehension to quickly generate lists:
# even numbers up to (not including), 10
evens_mod = [i for i in range(10) if i % 2 == 0]
print("Evens up to 10 using mod (%): ", evens_mod)
# also even numbers up to 10, but using the step parameter of range
evens_step = [i for i in range(0,10,2)]
print("Evens up to 10 using range step: ", evens_step)
# iterators can often also be cast directly to lists, same result as above
evens_list_cast = list(range(0,10,2))
print("Evens up to 10 using list casting: ", evens_list_cast)
# squared versions of numbers between 10 (included) and 20 (not included)
squares = [f"{i}**2 = {i**2}" for i in range(10,20)]
print("Squares from 10 up to 20: ")
for s in squares:
    print(s)
