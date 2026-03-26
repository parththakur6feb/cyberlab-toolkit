from modules.password_cracker.utils import get_pass
import string
import time
import itertools

def brute_force():
    password = get_pass()
    max_length = 6
    total_attempts = 0
    found = False
    chars = string.ascii_letters + string.digits + string.punctuation

    # perms = itertools.permutations(chars,length)

    start = time.perf_counter()
    for l in range(1,max_length+1):
        if found:
            break
        print(f"Searching combinations of length {l}...")
        combinations = itertools.product(chars,repeat=l)

        for i in combinations:
            guess = ("".join(i))
            total_attempts+=1
            if password == guess:
                print(f"found {guess} in {total_attempts} attempts")
                found = True
                break
    if not found:
        print("password not found")
    end = time.perf_counter()
    print(f"time taken: {end - start:.3f} seconds")
   