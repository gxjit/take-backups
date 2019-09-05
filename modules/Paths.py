from os.path import basename, dirname, join, exists
from os import mkdir

from .Data import copyData, getChecksums


def transformPaths(src, dest):
    checksums = getChecksums(src)
    return [
        [join(dest, str(checksums[dirname(path)]), basename(path)) for path in src],
        checksums,
    ]


def checkTargets(targets):
    if isinstance(targets, list):
        for dir in targets:
            targetDir = dirname(dir)
            if not exists(targetDir):
                mkdir(targetDir)
    else:
        if not exists(targets):
            mkdir(targets)


def backupData(src, dest):
    checkTargets(dest)
    getDest, checksums = transformPaths(src, dest)
    checkTargets(getDest)
    copyData(src, getDest)
    with open(join(dest, "checksum-mappings.log"), "a") as f:
        f.write(f"{str(checksums)}\n\n")


def restoreData(src, dest):
    getSrc, _ = transformPaths(dest, src)
    copyData(getSrc, dest)
