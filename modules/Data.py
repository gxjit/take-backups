from os import remove
from os.path import dirname, exists
from shutil import copy
from zlib import adler32


def computeChecksums(datum):
    return adler32(datum.encode("utf8")) & 0xFFFFFFFF


def getChecksums(paths):
    uniquePaths = set(map(dirname, paths))
    print("\n",uniquePaths)
    checksums = {path: computeChecksums(path) for path in uniquePaths}
    return checksums


def copyData(src, dest):
    print(src, dest)
    for i, file in enumerate(src):
        if exists(file):
            if exists(dest[i]):
                remove(dest[i])
            copy(file, dest[i])
            print(f"\nfile {i} Copying :\n{file}\nto:\n{dest[i]}")
