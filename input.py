#!/usr/bin/env python3

name = ""

# an empty string evaluates to false in python, so we keep asking until we get something
while not name:
    name = input("What is your name? Tell me: ")

# the .format method is another way of filling variables into string and was the main
# way before f""-strings were introduced, it can still be useful when you want to fill
# longer expressions in or want them in multiple places, as it supports naming the arguments

# without naming, just by position
print("Hello {}!".format(name))
# with naming in 2 positions, converting the name to uppercase first
print("How are you {n}? Can you hear me {n}?".format(n=name.upper()))

