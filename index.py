plain_text = input("What text would you like to Cipher?:")
keyword = input("What keyword would you like to use?:")

code_start_point = 65
plain_text_codes = [ord(char) for char in plain_text]
keyword_codes = [ord(char) for char in keyword]

for i in plain_text_codes:
    ciphered = []
    for x in keyword_codes:
        if ord(i) >= code_start_point:
            
            

print(plain_text_codes)