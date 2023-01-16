#!/usr/bin/env python3
import os
import sys

env = os.environ  # retrieve the environment the script runs in

try:
    # the " and ' characters can be mixed like below to not collide with the string
    # the f before the string makes it a 'format-string' where variables can be
    # inserted directly in curly braces, which makes it very readable
    print(f"Hello from Python, your name is: {env['NAME']}")
    sys.exit(0) # exit with 0, all went well
except KeyError:
    # if we end up here, env['NAME'] could not be looked up
    # but instead of crashing we catch the exception and give a nice error
    print(f"Hello from Python, your NAME env variable is not set :( .")
    sys.exit(1) # exit with 1, something went wrong
