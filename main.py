from modules.encryption.rsa import generate_keys, encrypt, decrypt
from modules.encryption.caesar_cipher import caesar_encrypt,caesar_decrypt

while True:
    print("\n--- CyberLab Toolkit ---")
    print("1 Caesar Encrypt")
    print("2 Caesar Decrypt")
    print("3 RSA Encrypt")
    print("4 RSA Decrypt")
    print("5 Exit")

    try:
        choice = int(input("Choose: "))
    except ValueError:
        print("Enter a valid number")
        continue

    if choice == 5:
        print("Exiting...")
        break

    if choice not in range(1, 6):
        print("Invalid input")
        continue

    # Caesar
    if choice in (1, 2):
        text = input("Enter text: ")
        try:
            shift = int(input("Enter shift: "))
        except ValueError:
            print("Shift must be a number")
            continue

        if choice == 1:
            print("Encrypted:", caesar_encrypt(text, shift))
        else:
            print("Decrypted:", caesar_decrypt(text, shift))

    # RSA
    elif choice in (3, 4):
        try:
            p = int(input("Enter prime p: "))
            q = int(input("Enter prime q: "))
        except ValueError:
            print("Enter valid numbers")
            continue

        public_key, private_key = generate_keys(p, q)

        if choice == 3:
            msg = input("Enter message: ")
            cipher = encrypt(msg, public_key)
            print("Encrypted:", cipher)

        else:
            cipher = list(map(int, input("Enter cipher (space separated): ").split()))
            plain = decrypt(cipher, private_key)
            print("Decrypted:", plain)





    