import random
import time

def generate_random_number():
    while True:
        number = random.randint(10000000, 99999999)
        print(f"Generated Number: {number}")
        time.sleep(2)

if __name__ == "__main__":
    generate_random_number()