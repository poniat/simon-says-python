import random
import os
import time

colorRange = "RGBY"
simon = ""

os.system("cls")

for score in range(0, 10):
    simon += random.choice(colorRange)
    for color in simon:
        print(f"Simon says: {color}")
        time.sleep(1.5)
        os.system("cls")

    guess = input("What Simon said: ")
    os.system("cls")
    if guess != simon:
        break

print(f"Game over. Your final score is {score}!")
