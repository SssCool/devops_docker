import random
import time
import os

file_path = "/app/data/numbers.txt"

os.makedirs(os.path.dirname(file_path), exist_ok=True)

print("Random number generator started... Writing to", file_path)

while True:
    number = random.randint(10000000, 99999999) 
    with open(file_path, "a") as file:
        file.write(f"{number}\n")
    print(f"Generated and saved: {number}")
    time.sleep(2)