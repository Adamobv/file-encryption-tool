#user will have a file with material
from Crypto.Cipher import AES
from Crypto.Util.Padding import pad
from Crypto.Random import get_random_bytes


def padder(contents):
    extra = len(contents)%16
    if extra == 0:
        return contents
    else:
        pads_amount = 16-extra
        contents+=bytes([0x03]*pads_amount)
        return contents




def encrypt(filename,method):
    if method =="AES":
        contents = read_file(filename)
        if isinstance(contents, str):
            contents = contents.encode()  # Convert string to bytes
        contents = padder(contents)
        aes_key = get_random_bytes(16)
        #create the object that will encrypt using ECB
        cipher = AES.new(aes_key, AES.MODE_ECB)
        
        # Encrypt the data
        encrypted = cipher.encrypt(contents)
        inp = input("Enter the prefered filename for encrypted data: ")
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
    contents = ""
    try:
        with open(filename) as file:
            for line in file:
                contents +=line
    except FileNotFoundError:
        print("The file path is incorrect- Please try again")
    return contents


def decrypt(filename):
    pass


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
                decrypt(inp[1])
        else:
            print("Invalid command - type h for help menu")

main()