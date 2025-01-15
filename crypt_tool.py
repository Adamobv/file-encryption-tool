#user will have a file with material



def encrypt():


def decrypt():



def help_menu():
    print("h - Display this help menu")
    print("e - Encrypt a file")
    print("    Usage: encrypt <filepath> <method>")
    print("    method: Encryption method (e.g., AES, DES, etc.)")
    print()
    print("d - Decrypt an encrypted file")
    print("    Usage: decrypt <encrypted_filepath>")




       
def main():
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
        elif inp[0] == "e":
            if len(inp) < 3:
                print("Usage: encrypt <filepath> <method>")
            else:
                encrypt(inp[1], inp[2])
        elif inp[0] == "d":
            if len(inp) < 3:
                print("Usage: encrypt <filepath> <method>")
            else:
                decrypt(inp[1])
        else:
            print("Invalid command - type h for help menu")

main()