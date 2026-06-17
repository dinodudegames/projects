#attack simulator wthatever

import random

health = 100
kick = 15
punch = 10
heal = 20
enemy_health = 100
enemy = 0

def defeat():
    global health
    if health <= 0:
        print("you died!")
        fstats()
        return True



def kills():
    global enemy_health
    global enemy
    if enemy_health <=0:
        print("enemy defeated!")
        enemy += 1
        enemy_health = random.randint(50, 200)
        print(f"enemy health: {enemy_health}")

def fkick():
    x = random.randint(1,100)
    global health
    global enemy_health
    global kick
    enemy_health = enemy_health - kick
    if x > 50:
        health = health - 25
    return enemy_health, health

def fpunch():
    x = random.randint(1,100)
    global health
    global enemy_health
    global punch
    enemy_health = enemy_health - punch
    if x > 50:
        health = health - 25
    return enemy_health, health

def fheal():
    print("you healed of 20 points")
    global health
    health += 20
    return health

def fstats():
    global enemy
    print(f"you have defeated {enemy} enemies")
    

while True:
    print("-------------------------")
    print(f"you have {health} health")
    print(f"enemy has {enemy_health} health")
    print("-------------------------")
    print("what do you wish to do")
    print("-------------------------")
    print("kick - 1 (15 damage)")
    print("punch - 2 (10 damage)")
    print("heal - 3 (+20 health points)")
    print("quit - 4")

    try:
        choice = int(input("> "))
    except ValueError:
        print("invalid character")
        continue

    if choice == 1:
        fkick()
        kills()
        if defeat():
            break
    elif choice == 2:
        fpunch()
        kills()
        if defeat():
            break
    elif choice == 3:
        fheal()
    elif choice == 4:
        fstats()
        break
    else:
        print("cannot preceed")
        continue