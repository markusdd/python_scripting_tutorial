#!/usr/bin/env python3
from pathlib import Path
from subprocess import run
import sys

mydir = Path(__file__).parent
result = run(["ls", "-lah"], capture_output=True, cwd=mydir)

# when ls was successful, we run grep on the output by sending it into the stdin of grep
# this is basically the equivalent of a unix shell pipe, you could also send in stderr,
# which would then equate to a pipe in a unix shell with redirection
if result.returncode == 0:
    grep_result = run(["grep", "config.ini"], capture_output=True, input=result.stdout)
    print(grep_result.stdout.decode())
