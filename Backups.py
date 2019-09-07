from glob import glob
from sys import exit

from config import relativeDest, relativeSrc
from modules import areYouSure, backupData, flatMap, getInput, joinHomeTo, restoreData


def main():
    fullDestPaths = map(joinHomeTo, relativeSrc)
    backupSrc = flatMap(glob, fullDestPaths)
    backupDest = joinHomeTo(relativeDest)

    def backup():
        print("\nBacking up data...")
        areYouSure()
        backupData(backupSrc, backupDest)

    def restore():
        print("\nRestoring data...")
        areYouSure()
        restoreSrc, restoreDest = backupDest, backupSrc
        restoreData(restoreSrc, restoreDest)

    callbacks = [backup, restore, exit]
    print(
        (
            "\nWhat Should i do?"
            "\n0 -> Backup data."
            "\n1 -> Restore data."
            "\n2 -> Exit"
        )
    )

    getInput(callbacks)


if __name__ == "__main__":
    main()
