from sys import exit


def getInput(callbacks):
    try:
        choice = int(input("\n> "))
        if choice not in range(len(callbacks)):
            raise ValueError

    except ValueError:
        print("\nInvalid input.")
        getInput(callbacks)

    for i, callback in enumerate(callbacks):
        if choice == i:
            callback()
            return


def areYouSure():
    print("\nAre you sure you want to continue? (y/n)")
    try:
        choice = str(input("\n> ")).lower()
        if choice not in ["y", "n"]:
            raise ValueError
    except ValueError:
        print("\nInvalid input.")
        areYouSure()

    if choice == "y":
        return
    else:
        exit()
