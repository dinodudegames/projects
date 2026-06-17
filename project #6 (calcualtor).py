

#functions
def add(a,b):
    return a + b

def subtraction(a,b):
    return a - b

def multiplication(a,b):
    return a * b

def division(a,b):
    return a / b    

#while loop.
while True:
    print("what do you wish to do")
    print("----------------------")
    print("add - 1")
    print("subtract - 2")
    print("multiply - 3")
    print("devide - 4")
    print("exit - 0")

    try:
        choice = int(input("> "))
    except ValueError:
        print("invalid character")
        continue
    
    if choice == 0:
        break
    elif 5 <= choice <= 9:
        print("invalid character")
        continue
    
    try:
        num1 = float(input("first number: "))
        num2 = float(input("second number: "))
    except ValueError:
        print("invalid character")
        continue

    if choice == 1:
        number = add(num1,num2)
        print(number)
    elif choice == 2:
        number = subtraction(num1,num2)
        print(number)
    elif choice == 3:
        number = multiplication(num1,num2)
        print(number)
    elif choice == 4:
        if num2 == 0:
            print("cannot divide by 0")
            continue
        number = division(num1, num2)
        print(number)
    else: 
        print("invalid character")
        continue