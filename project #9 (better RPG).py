import random

player = {
    "health": 100,
    "coins": 50,
    "level": 1,
    "exp": 0,
}

player_inventory = ["health_potion", "health_potion"]

enemy_helath = 100
enemy_kill_count = 0
drop = 0


# ----------------- HEAL FUNCTIONS -----------------

def fhealth():
    if "health_potion" in player_inventory:
        player["health"] += 25
        player_inventory.remove("health_potion")
        return True
    return False


def fhuge_health():
    if "huge_health_potion" in player_inventory:
        player["health"] += 100
        player_inventory.remove("huge_health_potion")
        return True
    return False


# ----------------- ENEMY FUNCTION -----------------

def fenemy():
    global enemy_helath
    global enemy_kill_count
    global drop

    # if already dead before attack
    if enemy_helath <= 0:
        enemy_helath = random.randint(90, 200)
        enemy_kill_count += 1

        coin = random.randint(45, 200)
        player["coins"] += coin

        rdrop = random.randint(1, 100)

        if rdrop <= 50:
            player_inventory.append("health_potion")
            print("you got health potion")

        if rdrop <= 10:
            player_inventory.append("drop")
            drop += 1
            print("you got rare drop")

        exp = random.randint(25, 100)
        player["exp"] += exp

        if player["exp"] >= 100:
            player["level"] += 1
            player["exp"] -= 100
            player["coins"] += 100
            print(f"level up! now level {player['level']}")
        return

    # attack enemy
    dmg = random.randint(5, 50)
    enemy_helath -= dmg
    print(f"you dealt {dmg} damage to enemy!")

    #death check
    if enemy_helath <= 0:
        fenemy()
        return

    # enemy attacks back
    x = random.randint(1, 100)
    if x >= 50:
        dmg1 = random.randint(5, 40)
        player["health"] -= dmg1
        print(f"enemy dealt {dmg1} damage to you!")


# ----------------- END GAME STATS -----------------

def beforebreak():
    print(f"enemies defeated: {enemy_kill_count}")
    print(f"drops collected: {drop}")


# ----------------- MAIN LOOP -----------------

while True:

    if player["health"] > 0:
        for stats, value in player.items():
            print(stats, value)
        print(f"enemy health : {enemy_helath}")
    else:
        beforebreak()
        break

    print("1 - view inventory")
    print("2 - attack enemy")
    print("3 - shop")
    print("4 - heal +25")
    print("5 - heal +100")
    print("0 - exit")

    try:
        choice = int(input("> "))
    except ValueError:
        print("invalid character")
        continue

    if choice == 1:
        if len(player_inventory) == 0:
            print("inventory is empty")
        else:
            for items in player_inventory:
                print(items)

    elif choice == 2:
        fenemy()

    elif choice == 3:
        while True:
            print("1 - buy health potion (50 coins)")
            print("2 - buy huge health potion (150 coins + drop)")
            print("0 - exit shop")

            try:
                choice = int(input("> "))
            except ValueError:
                print("invalid character")
                continue

            if choice == 1:
                if player["coins"] >= 50:
                    player_inventory.append("health_potion")
                    player["coins"] -= 50
                    print("health potion bought!")
                else:
                    print("insufficient funds")

            elif choice == 2:
                if "drop" in player_inventory:
                    if player["coins"] >= 150:
                        player_inventory.append("huge_health_potion")
                        player_inventory.remove("drop")
                        print("huge health potion bought!")
                    else:
                        print("insufficient funds")
                else:
                    print("no drop in inventory")

            elif choice == 0:
                break

    elif choice == 0:
        beforebreak()
        break

    elif choice == 4:
        if fhealth():
            print("gained +25 health")
        else:
            print("no health potion")

    elif choice == 5:
        if fhuge_health():
            print("gained +100 health")
        else:
            print("no huge health potion")