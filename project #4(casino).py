import random

symbols = ["🍒", "🍋", "⭐"]
cartext = ["u got hella good car (got a car 🚗 )", "ayo that car lookin niceee (got a car 🚗 )", "yo is that a car??? (got a car 🚗 )"]

rolls = 0
jackpot = 0
mini_win = 0
coins = 100
car = 0
work = 0
#🪙

while True:

    print("roll - 1 (10🪙 )")
    print("work - 2")
    print("get the car gng - 3")
    print("exit - 0")
    print(" ")
    
    print(f"you have {coins}🪙")
    

    #input

    try:
        choice = int(input("> "))
    except ValueError:
        print("invalid character")
        continue
    
    #choice

    if choice == 1:
            
        if coins >=10:
            coins -= 10
        else:
            print("insufficient funds")    
            continue

            # random choice

        a = random.choice(symbols)
        b = random.choice(symbols)
        c = random.choice(symbols)
        print(a, b, c)
        rolls += 1

        #tier system

        if a == b == c:
            print("JACKPOT!!!")
            jackpot += 1
            coins += 100
        elif a == b and a != c  or b == c and b != a:
            print("mini Win")
            coins += 15
            mini_win += 1
        else:
            continue

    elif choice == 0:
        print(f"rolls: {rolls}")
        print(f"work : {work}")
        print(f"mini wins: {mini_win}")
        print(f"jackpots: {jackpot}")
        print(f"cars😎: {car}")
        break

    elif choice == 2:
        salary = random.randint(1, 50)
        coins = coins + salary
        print(f"you worked and gained {salary}🪙")
        work += 1
        
        #car

    elif choice == 3:
        while True:
            print("proceed to buy a car?")
            print("yes - 1")
            print("no - 2")
            
            
            buy_car = int(input("> "))

            if buy_car == 1:
                if coins >= 1500:
                    coins -= 1500
                    car += 1
                    print(random.choice(cartext))
                else:
                    print("insufficient funds")
                    continue

            elif buy_car == 2:
                print("oki doki")
                break


    else:
        print("cant proceed")
        continue


        