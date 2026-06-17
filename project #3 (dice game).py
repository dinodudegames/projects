#dice roller

import random
rolls = 0

while True:

    print("roll dice - 1")
    print("exit - 2")

    try:
        choice = int(input("what u wish to do:"))
    except ValueError:
        print("invalid character")
        continue

    if choice == 1:
        dice = random.randint(1,6)
        print(dice)
        rolls += 1

    elif choice == 2:
        print(f"you have rolled {rolls} times")
        break
    else:
        print("invalid character")
        continue
