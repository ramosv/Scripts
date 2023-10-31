#!/usr/bin/python3

import os, sys
from stat import *


# Output should be in the format of find /usr/bin -name '*mk*' -print


def myFind(top, afile):
    root = os.listdir(top)
    size = 0

    for f in root:
        path = os.path.join(top, f)
        mode = os.lstat(path).st_mode

        if afile not in path:
            continue
        else:
            if S_ISDIR(mode):
                # If the function does find a directory then use recursion to look into it
                size += myFind(path, afile)
            elif S_ISREG(mode):
                # No more directories to recurse into. It must be a file.
                fileName = path
                info = os.stat(path)
                print(f"{fileName} -------------- {info.st_size} bytes")

    return size


if __name__ == "__main__":
    first = sys.argv[1]
    second = sys.argv[2]

    myFind(first, second)
