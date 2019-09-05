def getInput(callbacks):
    while True:
        try:
            choice = int(input("\n> "))
            if choice not in range(len(callbacks)):
                raise ValueError

        except ValueError:
            print("\nInvalid input.")
            continue

        for i, callback in enumerate(callbacks):
            if choice == i:
                callback()
                return
