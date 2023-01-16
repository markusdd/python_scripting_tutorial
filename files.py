#!/usr/bin/env python3

from pathlib import Path
import os

# compared to the sys_os.py script, the get method never 'crashes',
# but returns None if TARGET_DIR would be undefined
home = os.environ.get("TARGET_DIR")

basepath = Path("/tmp" if not home else home)

folders = [("dir1", "subdir1"),
           ("dir2", "subdir2"),
           ("dir3", "subdir3")]

files = ["a.txt", "b.txt", "c.txt"]

# we iterate like in path.py, but just have the list folders, which is a list of tuples now
# python allows us to 'unpack' these the same way when we used zip
for t, s in folders:
    fullpath = basepath / t / s
    # calling makedirs with exist_ok set to true behaves like the well know 'mkdir -p'
    os.makedirs(fullpath, exist_ok=True)
    for file in files:
        # open the filepath for writing,
        # this will truncate the file contents if it existed before
        with open(fullpath / file, 'w') as filehandle:
            filehandle.writelines([f"Hi, I am the file {file}.\n", "\n", "Isn't this cool?\n"])
