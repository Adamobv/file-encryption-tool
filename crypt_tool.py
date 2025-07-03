    #user will have a file with material
from Crypto.Cipher import AES
from Crypto.Protocol.KDF import PBKDF2
from Crypto.Util.Padding import pad
from Crypto.Random import get_random_bytes
import hashlib


def padder(contents):
    extra = len(contents)%16
    pads_amount = 16-extra
    if pads_amount == 0:
        pads_amount=16

    for pad in range(pads_amount):
        contents+= bytes([pads_amount])
    return contents

# practiced PKCS#7 which is the currrent standard for padding in AES etc.
# I was able to use predone classes imported to have the compliant padding predone but instead
# - I made sure to do the PKCS#7 manually and work through each step of identifying how muhc padding should be added
# (Public-Key Cryptography Standards #7)


def processor(filename):
    contents = read_file(filename)
    if isinstance(contents, str):
        contents = contents.encode()  # Convert string to bytes
    contents = padder(contents)
    base_salt = get_random_bytes(16) 
    #adding salt will make it so two users with same password will have different keys

    password = input("Enter a Password: ")
    aes_key = PBKDF2(password, base_salt, dkLen=16)
    return aes_key , contents, base_salt
    #create the object that will encrypt using ECB

#practiced making salts to ensure rainbow tables cannot be used to bruteforce a keya nd decrypt the data
#allowed me to include teh addition of a password to the data for security instead of encrypting and decrypting data raw



def hash_contents(contents):
    sha256_hash = hashlib.sha256()  # Creates a SHA-256 hash object
    sha256_hash.update(contents)
    return  sha256_hash.digest()
# practiced HASHING data and checking the hash when decrypting to ensure the signature is correct 
# and the password is the same



def encrypt(filename,method):
    if method =="AES":

        inp = input("Enter the prefered filename for encrypted data: ")

        processes = processor(filename)
        aes_key = processes[0]
        salt = processes[2]
        contents = processes[1]
        
        # Encrypt the data
        cipher = AES.new(aes_key, AES.MODE_ECB)
        encrypted = cipher.encrypt(contents)+hash_contents(contents)+salt
        create_enc_file(encrypted,inp+".txt")

    elif method =="DES":
        pass
    else:
        print("Invalid method")




def create_enc_file(encrypted, filename):
    try:
        with open(filename, 'wb') as file:
            file.write(encrypted)
        print("File successfully saved in: ",filename)
    except Exception as e:
        print("Error while saving file")




def read_file(filename):
    try:
        with open(filename, 'rb') as f:
            return f.read()      # returns a bytes object
    except FileNotFoundError:
        print("The file path is incorrect- Please try again")
        return b""              # empty bytes on failure



def un_padder(contents):
    excess = contents[-1]
    contents = contents[:-excess]
    return contents



def decrypt(filename,method):
    if method == "AES":

        password = input("Enter the password used to origionally encrypt: ")

        while True:           
            crypted_contents = read_file(filename)
            salt = crypted_contents[-16:]
            message = crypted_contents[:-48]
            hashh = crypted_contents[-48:-16]
            aes_key = PBKDF2(password, salt, dkLen=16)
            
            cipher = AES.new(aes_key, AES.MODE_ECB)
            decrypted_padded =cipher.decrypt(message)
        
            if hash_contents(decrypted_padded) != hashh:
                password = input("Incorrect password, please try again: ")
                continue
#
# i learned that this form of using a hash does not encapsulate data integreity, since someone can fake a hash in there
#
            else:
                inp = input("Enter the prefered filename for decrypted file: ")
                create_enc_file(un_padder(decrypted_padded),inp+".txt")
                break
        print("Success")



def help_menu():
    print("\n")
    print("h - Display this help menu")
    print("e - Encrypt a file")
    print("    Usage: encrypt <filepath> <method>")
    print("    method: Encryption method (currently this program offers: 'AES' or 'DES')")
    print()
    print("d - Decrypt an encrypted file")
    print("    Usage: decrypt <encrypted_filepath> <method>")
    print("    method: Decryption method that was used")
    print("q - End this program \n")



    
def main():
    print("Type h for help display- ")
    while True:
        check=0
        raw=input("> ")
        inp=raw.split(" ")
        if inp[0] == "q":
            print("Watch an ad to earn an extra life?")
            print("Goodbye!")
            break            
        elif inp[0] == "h":
            help_menu()
        elif inp[0] == "encrypt":
            if len(inp) < 3:
                print("Usage: encrypt <filepath> <method>")
            else:
                encrypt(inp[1], inp[2])
        elif inp[0] == "decrypt":
            if len(inp) < 3:
                print("Usage: encrypt <filepath> <method>")
            else:
                decrypt(inp[1],inp[2])
        else:
            print("Invalid command - type h for help menu")

main()