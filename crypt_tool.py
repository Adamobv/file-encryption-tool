#user will have a file with material







def help_menu():
    print("h - Display this help menu")
    print("e - Encrypt a file")
    print("    Usage: encrypt <filepath> <method>")
    print("    filepath: Path to the file to encrypt (e.g., my_file.txt)")
    print("    method: Encryption method (e.g., AES, DES, etc.)")
    print("d - Decrypt an encrypted file")
    print("    Usage: decrypt <encrypted_filepath>")
    print("    encrypted_filepath: Path to the encrypted file (e.g., my_file.txt.enc)")




       
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
           pass
        elif inp[0] == "d":
            pass

main()