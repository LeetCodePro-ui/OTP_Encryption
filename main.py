import secrets
import sys

banner = r'''
   ______  ___________  _______    __    _______  _____  ___    ______    _______   ___  ___  _______   
   /    " \("     _   ")|   __ "\  /""\  /"     "|(\"   \|"  \  /" _  "\  /"      \ |"  \/"  ||   __ "\  
  // ____  \)__/  \\__/ (. |__) :)//   \(: ______)|.\\   \    |(: ( \___)|:        | \   \  / (. |__) :) 
 /  /    ) :)  \\_ /    |:  ____//'_/\_\\\/    |  |: \.   \\  | \/ \     |_____/   )  \\  \/  |:  ____/  
(: (____/ //   |.  |    (|  /            // ___)_ |.  \    \. | //  \ _   //      /   /   /   (|  /      
 \        /    \:  |   /|__/ \          (:      "||    \    \ |(:   _) \ |:  __   \  /   /   /|__/ \     
  \"_____/      \__|  (_______)          \_______) \___|\____\) \_______)|__|  \___)|___/   (_______)    

       
'''
print(banner)
print("\n\n")

def encrypt(i,key):
     #1:turning character i into ASCII number
     #2:Subtracting 32, adding key
     #3:mod 95 to receive number in ASCII scale, adding 32 to not leave printable character scale
    return chr((ord(i) - 32 +key) % 95 + 32)
def decrypt(i,key):
    return chr((ord(i) - 32 -key) % 95 +32)
while True:
    try:
        while True:
            choice = input("\nPlease enter your choice:\n1:END Program\n2:Encryption\n3:Decryption\n")
            if choice == str(1):
                print("\n--- Program finished ---")
                sys.exit()
            elif choice == "2" or choice == "3":
                break
            else:
                print("ERROR\nEnter a valid option!\n")
                continue


        if choice == str(2):
            txt = input("Enter your text for encryption here.\n")


            print("\n--- Running Encryption ---")
            #generating empty list and string for following loop
            key_list = []
            enc_txt = ""
    
    
            for i in txt:
            #secret number until 95 because of printable ASCII characters
                key = secrets.randbelow(95)
                key_list.append(key)        
                enc_txt += encrypt(i,key)
            key_str = ""
            for j in key_list:
                key_str += chr(j + 32)

            print(f"Encrypted text:\n{enc_txt}\n\n")
            print(f"Encryption key:\n{key_str}\n\n")
            print("\n--- Program finished ---\n")
        
        elif choice == str(3):
            dec_txt = input("Enter your encrypted text here:\n\n")
            dec_key = input("Enter your key here:\n\n")
            enc = ""
            txt_key = zip(dec_txt,dec_key)

            for k,l in txt_key:
                key_int = ord(l) - 32
                enc += decrypt(k,key_int)



            print(f"\nDecrypted text:{enc}\n")
            print("\n--- Program finished ---\n")


            




    except KeyboardInterrupt:
        print("\n--- KeyboardInterrupt ---")
        print("\n--- Program finished ---")
        break



