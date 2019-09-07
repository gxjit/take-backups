from os import mkdir
from os.path import basename, dirname, exists, join

from .Data import copyData, getChecksums
from .Helpers import globPaths


def transformPaths(src, dest):
    checksums = getChecksums(src)
    return [
        [join(dest, str(checksums[dirname(path)]), basename(path)) for path in src],
        checksums,
    ]


def transformDestPaths(globbedSrc, checksums):
    checksumsLookup = {value: key for key, value in checksums.items()}
    return [
        join(checksumsLookup[int(basename(dirname(path)))], basename(path))
        for path in globbedSrc
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
    globbedSrc = globPaths(src)
    nwDest, checksums = transformPaths(globbedSrc, dest)
    checkTargets(nwDest)
    with open(join(dest, "checksum-mappings.log"), "a") as f:
        f.write("\n----\n" f"{str(src)}" "\n-\n" f"{str(checksums)}" "\n----\n")
    # print(globbedSrc, "\n\n", nwDest)
    copyData(globbedSrc, nwDest)


def restoreData(src, dest):
    nwSrc, checksums = transformPaths(dest, src)
    globbedSrc = globPaths(nwSrc)
    originDest = transformDestPaths(globbedSrc, checksums)
    # print(globbedSrc, "\n\n", originDest)
    copyData(globbedSrc, originDest)
