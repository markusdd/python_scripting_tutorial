#!/usr/bin/env python3

from pathlib import Path
import os

# compared to the sys_os.py script, the get method never 'crashes',
# but returns None if TARGET_DIR would be undefined
home = os.environ.get("TARGET_DIR")

# if the TARGET_DIR env variable is set we use it, otherwise we use /tmp as default
basepath = Path("/tmp" if not home else home)

topfolders = ["Pictures", "Downloads", "Documents"]
subfolders = [".thumbnails", ".cache", ".tmp"]

# a bit senseless in this example, but good for demonstration
# we 'zip' both lists together and with each iteration we get
# the pairing of the topfolder and the subfolder we want to create
for t, s in zip(topfolders, subfolders):
    # the path class 'overloads the division symbol so you can attach further
    # path components by simply 'dividing' the path by a string
    fullpath = basepath / t / s
    # calling makedirs with exist_ok set to true behaves like the well know 'mkdir -p'
    os.makedirs(fullpath, exist_ok=True)
