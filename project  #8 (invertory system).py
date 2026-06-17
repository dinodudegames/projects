#invertory

invertory = []

def add():
    global invertory
    item = input("what do u wish to add: ")
    invertory.append(item)

def remove():
    global invertory
    item = input("what do you wish to remove: ")

    if item in invertory:
        invertory.remove(item)
    else:
        print("no such item in invetory")
        return False

while True:

    print("veiw invertory - 1")

    if len(invertory) == 0:
        print("invertory is empty")
    else:
        print(f"invertory contains {len(invertory)} items")

    print("add item to invertory - 2")
    print("remove item from invertory - 3")
    print("exit - 0")

    try:
        choice = int(input("> "))
    except ValueError:
        print("invalid character")
        continue

    if choice == 1:
        for items in invertory:
            print(items)
        continue
    elif choice == 2:
        add()
    elif choice == 3:
        remove()
    elif choice == 0:
        break
    else:
        print("cannot proceed")
        continue