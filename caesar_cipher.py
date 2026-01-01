def encrypt(text, shift):
    encrypted_text = ""
    for char in text:
        if char.isalpha(): 
            shift_base = 65 if char.isupper() else 97 
            encrypted_text += chr((ord(char) + shift - shift_base) % 26 + shift_base)
        else:
            encrypted_text += char 
    return encrypted_text
def decrypt(text, shift):
    decrypted_text = ""
    for char in text:
        if char.isalpha():
            shift_base = 65 if char.isupper() else 97
            decrypted_text += chr((ord(char) - shift - shift_base) % 26 + shift_base)
        else:
            decrypted_text += char
    return decrypted_text
if __name__ == "__main__":
    while True:
        print("  \nCaesar Cipher Encryption & Decryption \n ")
        print("\nOptions:")
        print("1. Encrypt a message")
        print("2. Decrypt a message")
        print("3. Exit\n")
        choice = input("Enter your choice : ")
        if choice == '1':
            message = input("Enter the message to encrypt: ")
            shift_value = int(input("Enter the shift value: ")) 
            print("\nOriginal message:", message)
            print("Shift value:", shift_value)
            encrypted_message = encrypt(message, shift_value)
            print("Encrypted message:", encrypted_message)
        elif choice == '2':
            message = input("Enter the message to decrypt: ")
            shift_value = int(input("Enter the shift value: ")) 
            print("\nOriginal message:", message)
            print("Shift value:", shift_value)
            decrypted_message = decrypt(message, shift_value)
            print("Decrypted message:", decrypted_message)
        elif choice == '3':
            print("Exiting the program.")
            break  
        else:
            print("Invalid choice, please enter a number between 1 and 3.")
