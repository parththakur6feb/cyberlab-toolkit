import sys

def get_pass(limit=6):
    while True:
        pwd = input("Enter password (or 'q' to cancel): ")
        
        if pwd.lower() == 'q':
            sys.exit()
        
        if 0 < len(pwd) <= limit:
            return pwd
            
        print(f"Invalid length! Password must be 1-{limit} characters.")
