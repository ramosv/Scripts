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


# linuxadmin@LinuxMint:~/Desktop/Python$ ./myFind.py /usr/bin mk
# /usr/bin/mkmanifest -------------- 14720 bytes
# /usr/bin/unmkinitramfs -------------- 3774 bytes
# /usr/bin/mkdiskimage -------------- 8792 bytes
# /usr/bin/mkzftree -------------- 31016 bytes
# /usr/bin/mknod -------------- 43520 bytes
# /usr/bin/grub-mklayout -------------- 258224 bytes
# /usr/bin/grub-mknetdir -------------- 427680 bytes
# /usr/bin/mkdir -------------- 68096 bytes
# /usr/bin/grub-mkpasswd-pbkdf2 -------------- 262352 bytes
# /usr/bin/mk_modmap -------------- 16163 bytes
# /usr/bin/grub-mkimage -------------- 369712 bytes
# /usr/bin/grub-mkstandalone -------------- 505808 bytes
# /usr/bin/grub-mkfont -------------- 278960 bytes
# /usr/bin/mkfifo -------------- 39424 bytes
# /usr/bin/mkfontscale -------------- 43696 bytes
# /usr/bin/grub-mkrelpath -------------- 253520 bytes
# /usr/bin/grub-mkrescue -------------- 1022432 bytes
# /usr/bin/mksquashfs -------------- 260792 bytes
# /usr/bin/mktemp -------------- 39424 bytes
# /usr/bin/ipcmk -------------- 22976 bytes
# /usr/bin/mkfontdir -------------- 65 bytes
# linuxadmin@LinuxMint:~/Desktop/Python$ ./myFind.py /usr/bin mk
# /usr/bin/mkmanifest -------------- 14720 bytes
# /usr/bin/unmkinitramfs -------------- 3774 bytes
# /usr/bin/mkdiskimage -------------- 8792 bytes
# /usr/bin/mkzftree -------------- 31016 bytes
# /usr/bin/mknod -------------- 43520 bytes
# /usr/bin/grub-mklayout -------------- 258224 bytes
# /usr/bin/grub-mknetdir -------------- 427680 bytes
# /usr/bin/mkdir -------------- 68096 bytes
# /usr/bin/grub-mkpasswd-pbkdf2 -------------- 262352 bytes
# /usr/bin/mk_modmap -------------- 16163 bytes
# /usr/bin/grub-mkimage -------------- 369712 bytes
# /usr/bin/grub-mkstandalone -------------- 505808 bytes
# /usr/bin/grub-mkfont -------------- 278960 bytes
# /usr/bin/mkfifo -------------- 39424 bytes
# /usr/bin/mkfontscale -------------- 43696 bytes
# /usr/bin/grub-mkrelpath -------------- 253520 bytes
# /usr/bin/grub-mkrescue -------------- 1022432 bytes
# /usr/bin/mksquashfs -------------- 260792 bytes
# /usr/bin/mktemp -------------- 39424 bytes
# /usr/bin/ipcmk -------------- 22976 bytes
# /usr/bin/mkfontdir -------------- 65 bytes
# linuxadmin@LinuxMint:~/Desktop/Python$
