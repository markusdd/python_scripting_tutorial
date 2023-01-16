#!/usr/bin/env python3
from configparser import ConfigParser
import sys

# in this example we use configparser, which supports an INI-like structure
# there is also support for default and fallback values etc.
# see the full spec here: https://docs.python.org/3/library/configparser.html
cfg = ConfigParser()
cfg.read("config.ini")

if not "credentials" in cfg:  # some error handling is always good practice
    print("Error: No credentials section in config.ini .")
    sys.exit(1)
else:
    cred = cfg["credentials"]

name = cred.get("name")
age = cred.get("age")
city = cred.get("city")
if not name or not age or not city:
    print("Error: Malformed config, name, city or age missing.")
    sys.exit(1)

print(f"{name} lives in {city} and is {age} years old.")
