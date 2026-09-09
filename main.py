import secrets


banner = r"""
  ____   _____  _____     ______                   _____            _ 
 / __ \ |_   _||  __ \   |  ____|                 / ____|          | |
| |  | |  | |  | |__) |  | |__   _ __   ___  _   | (___   _   _ ___| |
| |  | |  | |  |  ___/   |  __| | '_ \ / __|| |   \___ \ | | | / __| |
| |__| | _| |_ | |      _| |____| | | | (__ | |   ____) || |_| \__ \_|_
 \____/ |_____||_|     (_)______|_| |_|\___||_|  |_____/  \__, |___(_)
                                                           __/ |      
                                                          |___/       
"""
print(banner)
print("\n\n")
while True:
    choice = input("Please enter your choice:\n1:Encryption\n")
    if choice == str(1):
        break
    else:
        print("ERROR\nEnter a valid option!")
        continue

if choice == str(1):
    txt = input("Enter your text for encryption here.\n")
    txt = txt.lower()

    print("\n--- Running Encryption ---")
    
    key_list = []
    enc_txt = ""
    
    for i in txt:
        key = secrets.randbelow(95)
        key_list.append(key)
        enc_txt += chr((ord(i) - 32 +key) % 95 + 32)
    print(enc_txt)
    print(key_list)

