import string
def gcd(a,b):
    while b:
        a, b = b, a % b
    return a

def find_e(phi):
    e = 2
    while e < phi:
        if gcd(e,phi) == 1:
            return e
        e+=1

def find_d(e,phi):
    d = 1
    while True:
        if (d*e) % phi == 1:
            return d
        d+=1

def generate_keys(p,q):
    n = p*q
    phi = (p-1)*(q-1)
    e = find_e(phi)
    d = find_d(e,phi)
    return (e, n), (d, n)

def encrypt(message,public_key):
    e, n = public_key
    return[pow(ord(char), e, n) for char in message]

def decrypt(cipher,private_key):
    d, n = private_key
    return "".join([chr(pow(char, d, n)) for char in cipher])