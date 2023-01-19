#!/usr/bin/env python3

def main():
    print("Hello from main.")

# only execute our code if we are the script that has been called as the main program
# this mainly makes sense if you re-use the code of some functions or even main
# in another python module, otherwise on import the code immidiately executes, which usually
# is not what you want
# for single-file scripts, it is often recommended, but not strictly necessary
if __name__ == "__main__":
    main()
