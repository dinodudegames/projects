# ---------- to do list ------------
tasks = []

def task_list():
        if len(tasks) > 0 :

            for i in range(len(tasks)):
                print(f"{i + 1}) {tasks[i]}")
        
        else:
            print("no tasks")

def add_item():
    task = input("add task: ")
    tasks.append(task)

def remove_item():

    task_list()
    
    if len(tasks) > 0:

        try:
           task = int(input("which task to remove? (input number) : "))
        except ValueError:
            print("invalid character")
            return
            
        index = task - 1

        if 0 <= index < len(tasks):
            tasks.pop(index)
            print(f"removed task") 

        else:
            print("no such task in tasks")


while True:

    print("1 - veiw tasks")
    print("2 - add tasks")
    print("3 - remove tasks")
    print("0 - exit")

    try:
        choice = int(input("> "))
    except ValueError:
        print("invalid character")
        continue

    if choice == 1:
        task_list()

    elif choice == 2:
        add_item()

    elif choice == 3:
        remove_item()

    elif choice == 0:
        task_list()
        break
            