from modules.password_cracker.utils import get_pass
import time

def dictionary_attack():
    try:
        path = r"modules\password_cracker\file.txt"
        password = get_pass(15)

        start = time.perf_counter()
        with open(path,"r") as file:
            for count,line in enumerate(file,1):
                guess = line.strip()
                if password == guess:
                    print(f"found {guess} in {count} attempts")
                    break
            else:
                print("password not found")
            end = time.perf_counter()
            print(f"time taken: {end - start:.5f} seconds")
    except FileNotFoundError:
        print(f"Error: Could not find the file at {path}")
            