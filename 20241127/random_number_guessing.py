import random

target_number = random.randint(1, 100)

while True:
    guess_number = int(input("Enter a mumber :"))

    if guess_number < target_number:
        print("Too low!")
    elif guess_number > target_number:
        print("Too High")
    else:
        print("Correct! The number was", target_number)
        break
