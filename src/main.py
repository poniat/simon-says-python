import random
import os
import time

colorRange = "RGBY"
simon = ""

os.system("cls")

sleepTimeInSeconds = 0

while sleepTimeInSeconds == 0:
    print(f"Welcome to SIMON SAYS game.")
    print(f"Select difficulty:")
    print(f" 1 - easy / slow")
    print(f" 2 - normal")
    print(f" 3 - hard / fast")

    difficulty = input("Choise: ")

    if difficulty == "1":
        sleepTimeInSeconds = 2
    elif difficulty == "2":
        sleepTimeInSeconds = 1.5
    elif difficulty == "3":
        sleepTimeInSeconds = 1

os.system("cls")

for score in range(0, 10):
    simon += random.choice(colorRange)
    for color in simon:
        print(f"Simon says: {color}")
        time.sleep(sleepTimeInSeconds)
        os.system("cls")

    guess = input("What Simon said: ")
    os.system("cls")
    if guess != simon:
        break

print(f"Game over. Your final score is {score}!")
