import random
number =random.randint(1,100)
attempts = 0

while True:
    
    try:
        guess=int(input("guess:"))
    except ValueError:
         print("invalid character")
         continue
    
    attempts += 1

    if guess < number:
        print("higher")
    
    elif guess > number :
          print("lower")
    
    else:
         print("thats Correct!")
         attempts += 1
         print(f"it took you {attempts} attempts")
         break