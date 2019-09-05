from glob import glob
from os.path import exists, expanduser, join
from sys import exit

from modules import backupData, getInput, restoreData


def main():
    relativeSrc = [
        ".config/sublime-text-3/Packages/User/*.sublime-build",
        ".config/sublime-text-3/Packages/User/*.sublime-settings",
        ".config/sublime-text-3/Packages/User/*.sublime-keymap",
        "Configs/.*",
    ]
    relativeDest = "Backups"  # src and dest are both relative to user home "~"
    backupDest = join(expanduser("~"), relativeDest)
    backupSrc = [
        file for path in relativeSrc for file in glob(join(expanduser("~"), path))
    ]

    def backup():
        print("\nBacking up data...")
        backupData(backupSrc, backupDest)

    def restore():
        print("\nRestoring data...")
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
