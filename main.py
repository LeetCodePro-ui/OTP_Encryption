import secrets
import sys
from datetime import datetime

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
            choice = input("\n[--Please enter your choice:--]\n1:END Program\n2:Encryption\n3:Decryption\n").strip()
            if choice == "1":
                print("\n--- Program finished ---")
                sys.exit()
            elif choice == "2" or choice == "3":
                break
            else:
                print("[--ERROR\nEnter a valid option!--]\n")
                continue


        if choice == "2":
            txt = input("[--Enter your text for encryption here.--]\n")


            print("\n--- Running Encryption ---")
            #generating empty list and string for following loop
            enc_txt = ""
            key_str = ""

            for i in txt:
            #secret number until 95 because of printable ASCII characters
                key = secrets.randbelow(95)
                key_str += chr(key + 32)
                enc_txt += encrypt(i,key)
            
                


            print(f"Encrypted text:\n{enc_txt}\n\n")
            print(f"Encryption key:\n{key_str}\n\n")

            while True:
                ask = input("""
[--Please enter your choice:--]
[--Save your encryption key and encrypted text in a .txt format = type 'save'--]
[--Repeat program = type 'continue'--]
[--End program = 'end'--]\n""").strip().lower()
                if ask == "save":
                    now = datetime.now()
                    timestamp = now.strftime("%Y-%m-%d-%H-%M-%S")
                    with open (f"encrypted_key_{timestamp}.txt","w", encoding = "utf-8") as f:
                        f.write(key_str)
                    with open (f"encrypted_text_{timestamp}.txt","w", encoding = "utf-8") as g:
                        g.write(enc_txt)
                    print(f"[--Your encryption key && encrypted text have been saved as:\n{f.name}\n{g.name}--]")
                    break
    
                elif ask == "continue":
                    break
            
                elif ask == "end":
                    sys.exit()
            
                else:
                    print("[--\nERROR\nEnter a valid option--]")
                    continue

        elif choice == "3":
            choi = input("\n[--For reading key && text from files: 'file'\nFor typing both manually: 'man'--]\n").strip().lower()
            
            dec_txt = ""
            dec_key = ""

            if choi == "man":
                dec_txt = input("[--Enter your encrypted text here:--]\n\n")
                dec_key = input("[--Enter your key here:--]\n\n")
                
            elif choi == "file":
                try:
                    
                    path_txt = input("[--Paste your encrypted_text file path here:--]\n").strip().strip("\"'")
                    with open(path_txt, "r", encoding="utf-8") as t:
                        dec_txt = t.read().removesuffix("\n").removesuffix("\r")
                    
                    
                    path_key = input("[--Paste your encryption_key here:--]\n").strip().strip("\"'")
                    with open(path_key, "r",encoding="utf-8") as z:
                        dec_key = z.read().removesuffix("\n").removesuffix("\r")

                except FileNotFoundError:
                    print("[--ERROR\nFile not found!--]")
                    continue
            else:
                print("[--ERROR\nEnter a valid option!--]")
                continue
                    
            if len(dec_txt) != len(dec_key):
                print("[--ERROR\nKey length does not match the length of the encrypted text!--]")
                continue

            enc = ""
            txt_key = zip(dec_txt,dec_key)

            for k,l in txt_key:
                key_int = ord(l) - 32
                enc += decrypt(k,key_int)


            print(f"\n[--Decrypted text:{enc}--]\n")
            print("\n--- Program finished ---\n")



            


    except KeyboardInterrupt:
        print("\n--- KeyboardInterrupt ---")
        print("\n--- Program finished ---")
        sys.exit()



