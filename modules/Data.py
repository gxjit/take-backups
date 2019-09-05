from os import remove
from os.path import dirname, exists
from shutil import copy
from zlib import adler32


def getChecksums(paths):
    uniquePaths = set([dirname(path) for path in paths])
    checksums = {
        path: (adler32(path.encode("utf8")) & 0xFFFFFFFF) for path in uniquePaths
    }
    return checksums


def copyData(src, dest):
    for i, file in enumerate(src):
        if exists(file):
            if exists(dest[i]):
                remove(dest[i])
            copy(file, dest[i])
            print(f"\nfile {i} Copying :\n{file}\nto:\n{dest[i]}")
