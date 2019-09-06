from os.path import basename, dirname, join, exists
from os import mkdir

from .Data import copyData, getChecksums


def transformPaths(src, dest):
    checksums = getChecksums(src)
    return [
        [join(dest, str(checksums[dirname(path)]), basename(path)) for path in src],
        checksums,
    ]


def mkdirNotExists(dirToMake):
    if not exists(dirToMake):
        mkdir(dirToMake)


def checkTargets(targets):
    if isinstance(targets, list):
        for dirs in targets:
            targetDir = dirname(dirs)
            mkdirNotExists(targetDir)
    else:
        mkdirNotExists(targets)


def backupData(src, dest):
    checkTargets(dest)
    getDest, checksums = transformPaths(src, dest)
    checkTargets(getDest)
    with open(join(dest, "checksum-mappings.log"), "a") as f:
        f.write(f"{str(checksums)}\n\n")
    copyData(src, getDest)


def restoreData(src, dest):
    getSrc, _ = transformPaths(dest, src)
    copyData(getSrc, dest)
