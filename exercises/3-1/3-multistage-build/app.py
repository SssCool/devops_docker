import time

file_path = "/app/numbers/numbers.txt"

print("Random Reader started...")

while True:
    try:
        with open(file_path, "r") as file:
            lines = file.readlines()
            if lines:
                last_number = lines[-1].strip()
                print(f"Random generator's last number is: {last_number}")
            else:
                print("No numbers found yet...")
    except FileNotFoundError:
        print("Waiting for numbers to be generated...")

    time.sleep(2)