#!/usr/bin/env python3
import argparse

parser = argparse.ArgumentParser(
             prog = 'argparse_input.py',
             description = 'Shows you what nice things argparse can do!',
         )
# positional, required arguments
parser.add_argument('name', type=str, help="Name of the caller.")
parser.add_argument('age', type=int, help="Age of the caller.")
# optional flag argument that does not take a value (true when given)
parser.add_argument('-u', '--uppercase', action="store_true")

args = parser.parse_args()

# uppercase the name if the flag has been given
if args.uppercase:
    name = args.name.upper()
else:
    name = args.name
# age is an integer, but python knows by itself to call the string representation of it
print(f"{name} is {args.age} years old.")
