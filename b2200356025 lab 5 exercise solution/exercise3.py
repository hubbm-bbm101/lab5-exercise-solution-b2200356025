import random

n = random.randint(0, 100)
is_found = False
while not is_found:
    guess = int(input("make a guess"))
    if guess < n:
        print("increase your number")
    elif guess > n:
        print("decrease your number")
    else:
        print("you found it!")
        is_found = True
      