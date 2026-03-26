import string
import itertools
import sys
import time

def estimated_time():
    password = get_pass(15)
    has_upper   = any(letter.isupper() for letter in password) 
    has_lower   = any(letter.islower() for letter in password)
    has_digit   = any(letter.isdigit() for letter in password)
    has_symbol  = any(not letter.isalnum() for letter in password)

    l = 0
    if has_upper:  l += len(string.ascii_uppercase)
    if has_lower:  l += len(string.ascii_lowercase)
    if has_digit:  l += len(string.digits)
    if has_symbol: l += len(string.punctuation)

    p = len(password)

    total_comb = sum(l**i for i in range(1,p+1))

    guesses_per_sec = 10_000_000
    est_seconds = total_comb / guesses_per_sec

    if est_seconds < 60:
        print(f"Estimated time: {est_seconds:.2f} seconds")
    elif est_seconds < 3600:
        minutes = est_seconds / 60
        print(f"Estimated time: {minutes:.2f} minutes")
    elif est_seconds < 86400:
        hours = est_seconds / 3600
        print(f"Estimated time: {hours:.2f} hours")
    else:
        days = est_seconds / 86400
        if days < 365:
            print(f"Estimated time: {days:.2f} days")
        else:
            years = days / 365
            print(f"Estimated time: {years:.2f} years")
        


def pass_strength():
    password = get_pass() 
    has_upper   = any(letter.isupper() for letter in password)
    has_lower   = any(letter.islower() for letter in password)
    has_digit   = any(letter.isdigit() for letter in password)
    has_symbol  = any(not letter.isalnum() for letter in password)
    
    is_not_repetitive = len(set(password)) > 1

    if is_not_repetitive and has_digit and (has_upper or has_lower):
        if has_symbol:
            print("Strength: STRONG (includes symbols)")
        else:
            print("Strength: MEDIUM (letters and numbers only)")
            print("Include symbols for better password")
    else:
        print("Strength: WEAK (missing variety or too repetitive)")
        print("Include symbols and numbers for better password")

def get_pass(limit=6):
    while True:
        pwd = input("Enter password (or 'q' to cancel): ")
        
        if pwd.lower() == 'q':
            sys.exit()
        
        if 0 < len(pwd) <= limit:
            return pwd
            
        print(f"Invalid length! Password must be 1-{limit} characters.")


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
        end = time.perf_counter()
        print("password not found")
        print(f"time taken: {end - start:.3f} seconds")
    

while True: 
    print("press 1 for dictionary brute force: ")
    print("press 2 for raw brute force: ")
    print("press 3 for password strength check: ")
    print("press 4 for password cracking estimated time: ")
    print("press 5 to exit.")
    try:
        inp = int(input("enter value: "))
    except(ValueError):
        print("enter valid value")
        continue


    if inp == 1:
        try:
            path = r"modules\password_cracker\file.txt"
            password = get_pass()

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
                
    elif inp == 2:
        brute_force()
    elif inp == 3:
        pass_strength()
    elif inp == 4:
        estimated_time()
    elif inp == 5:
        sys.exit()
    else:
        print("invalid input")
        continue
