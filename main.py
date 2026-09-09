import secrets


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
    return chr((ord(i) - 32 +key) % 95 + 32)

while True:
    try:
        while True:
            choice = input("Please enter your choice:\n1:Encryption\n")
            if choice == str(1):
                break
            else:
                print("ERROR\nEnter a valid option!")
                continue


        if choice == str(1):
            txt = input("Enter your text for encryption here.\n")


            print("\n--- Running Encryption ---")
            #generating empty list and string for following loop
            key_list = []
            enc_txt = ""
    
    
            for i in txt:
            #secret number until 95 because of printable ASCII characters
                key = secrets.randbelow(95)
                key_list.append(key)
                #1:turning character i into ASCII number
                #2:Subtracting 32, adding key
                #3:mod 95 to receive number in ASCII scale, adding 32 to not leave printable character scale
                enc_txt += encrypt(i,key)
            print(enc_txt)
            print(key_list)

    except KeyboardInterrupt:
        print("\n--- KeyboardInterrupt---")
        print("\n--- Program finished ---")
        break



