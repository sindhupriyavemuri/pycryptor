from cryptography.fernet import Fernet

def generate_key():
    return Fernet.generate_key()

def encrypt_file(key, input_file, output_file):
    with open(input_file, 'rb') as file:
        plaintext = file.read()
    
    f = Fernet(key)
    encrypted_data = f.encrypt(plaintext)
    
    with open(output_file, 'wb') as file:
        file.write(encrypted_data)

def decrypt_file(key, input_file, output_file):
    with open(input_file, 'rb') as file:
        encrypted_data = file.read()
    
    f = Fernet(key)
    decrypted_data = f.decrypt(encrypted_data)
    
    with open(output_file, 'wb') as file:
        file.write(decrypted_data)

# Main program
if __name__ == "__main__":
    print("PyCryptor is running...")
    
    encryption_key = generate_key()
    print("Generated Key:", encryption_key)
    
    input_file = input("Enter the path to the input file: ")
    output_file = input("Enter the path to the output file: ")
    
    encrypt_file(encryption_key, input_file, output_file)
    print("File encrypted successfully.")
    
    decrypt_file(encryption_key, output_file, "decrypted_file.txt")
    print("File decrypted successfully.")
