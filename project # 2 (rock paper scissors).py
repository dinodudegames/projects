import random

win = 0
lose = 0
tie = 0

while True:

    print("rock - 1")
    print("paper - 2")
    print("scissors - 3")
    print("exit - 0")

    choice = int(input())

    if choice == 1:
        player = "rock"

    elif choice == 2:
        player = "paper"

    elif choice == 3:
        player = "scissors"

    elif choice == 0:
        print("your starts")
        print(f"wins - {win}")
        print(f"loses - {lose}")
        print(f"ties - {tie}")
        break
    else:
        print("invalid input")
        continue
    hand = random.choice(["rock", "paper", "scissors"])

    print(f"{player} vs {hand}")
    
    if player == hand:
        print("Tie!")
        tie += 1
    
    elif (player == "rock" and hand == "scissors") or \
        (player == "paper" and hand == "rock") or \
        (player == "scissors" and hand == "paper"):
        print("You WIN!")
        win += 1

    else:
        print("You Lost...")
        lose += 1



