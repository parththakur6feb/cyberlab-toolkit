import string

def caesar_encrypt(text,shift):
    result = ""
    for ch in text.lower():
        if ch.isalpha():
            base = ord('a') if ch.lower() else ord('A')
            ch = chr((ord(ch) - base + shift) % 26 + base)
            result += ch
        else:
            result += ch
            continue
    return result

def caesar_decrypt(text,shift):
    result = ""
    for ch in text.lower():
        if ch.isalpha():
            base = ord('a') if ch.lower() else ord('A')
            ch = chr((ord(ch) - base - shift) % 26 + base)
            result += ch
        else:
            result += ch
            continue
    return result
