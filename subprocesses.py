#!/usr/bin/env python3
from pathlib import Path
from subprocess import run
import sys

# here we use the Python magic 'dunder' (double underscore) __file__, which is the
# location of the current python file
# using pathlib, we can easily get the directory where we are located
mydir = Path(__file__).parent

# arguments must be passed as a list with spaces omitted between them
# this is to ensure proper argument parsing and avoid any injection attacks
# capture_output does not just print the ls on the console, but collects everything
# for later use
# cwd sets the current working directory where the command should run
result = run(["ls", "-lah"], capture_output=True, cwd=mydir)
# try this line to see stderr
# result = run(["ls", "-lah", "doesnotexist"], capture_output=True, cwd=mydir)

# print also can take an arbitrary number of arguments, handy for something like this:
print("STDOUT: ", result.stdout.decode())

# stdout and stderr come as raw byte strings, so if you expect text you have to decode
# them, the default is usually fine (UTF-8)
print("STDERR: ", result.stderr.decode())

# we can collect exitcodes and pass it on upwards
print("Exit Code: ", result.returncode)
sys.exit(result.returncode)
