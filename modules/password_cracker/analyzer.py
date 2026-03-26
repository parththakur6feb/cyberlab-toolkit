from modules.password_cracker.utils import get_pass
import string

def pass_strength():
    password = get_pass(15) 
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

def estimated_time():
    password = get_pass(15)
    has_upper   = any(letter.isupper() for letter in password) 
    has_lower   = any(letter.islower() for letter in password)
    has_digit   = any(letter.isdigit() for letter in password)
    has_symbol  = any(not letter.isalnum() for letter in password)

    length = 0
    if has_upper:  length += len(string.ascii_uppercase)
    if has_lower:  length += len(string.ascii_lowercase)
    if has_digit:  length += len(string.digits)
    if has_symbol: length += len(string.punctuation)

    p_length = len(password)

    total_comb = sum(length**i for i in range(1,p_length+1))

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
