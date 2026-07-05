import json
path = "contacts/contacts.json"

#load old contacts

try:
    with open(path, "r") as file:
        contacts = json.load(file)
except FileNotFoundError:
    contacts = {}

#save function
def save():
    with open(path, "w") as file:
        json.dump(contacts, file)

contacts_count = 0 

#Main loop

while True:
    print("\n1 - Add contract\n2 - view contracts\n3 - search contract\n4 - delete contract\n0 - exit\n")
    print(f"you have {contacts_count} contacts saved")
    
    #askin for choice
    try:
        choice = int(input("> "))
    except ValueError:
        print("invalid character")
        continue

    #logic

    if choice == 1:
        name = input("name : ")
        try:
            number = int(input("number : "))
        except ValueError:
            print("wrong input type!")
            continue

        contacts[name] = number
        contacts_count += 1
        save()

    elif choice == 2:
        if len(contacts) >= 1:
            for name, number in sorted(contacts.items()):
                print(f"{name} : {number}")
        else:
            print("no contracts saved")

    elif choice == 3:
        contact_search = input("name : ")

        if contact_search in contacts:
            print(f"\n{contact_search} : {contacts[contact_search]}")
        else:
            print("\nNo such contact in dictonary")

    elif choice == 4:

        del_name = input("contact to delete : ")

        if del_name in contacts:
            del contacts[del_name]
            print("\nContact deleted successfully")
            contacts_count -= 1
            save()
        else:
            print("\nno such contact in dictonary")

    elif choice == 0:
        save()
        break