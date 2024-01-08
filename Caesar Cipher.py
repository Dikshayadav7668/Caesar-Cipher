# Caesar Cipher

alpahbet = ['a','b','c','d','e','f','g','h','i','j','k','l','m','n','o','p','q','r','s','t','u','v','w','x','y','z']

def encryption (plain_text,shift_key):
    cipher_text = ""
    for i in plain_text:
        if i in alpahbet:
            position = alpahbet.index(i)
            new_position = (position+int(shift_key))%26
            cipher_text +=alpahbet[new_position]
        else:
            cipher_text+=i
    print(f"Here is the text after encryption :- {cipher_text}")

def decryption(plain_text,shift_key):
    cipher_text = ""
    for i in plain_text:
        if i in alpahbet:
            position = alpahbet.index(i)
            new_position = (position-int(shift_key))%26
            cipher_text +=alpahbet[new_position]
        else:
            plain_text+=i
    print(f"Here is the text after the decryption: - {cipher_text}")
wanna_end=False
while not wanna_end:
    type=input(print("Type 'enrcypt' for encryption ,type 'decrypt' for description :\n " ))
    message = input("Type your message\n:-")
    shift  = input("Enter shift key\n")
    if type == "encrypt":
        encryption(plain_text=message,shift_key=shift)
    elif type == "decrypt":
        decryption(message,shift)
    play_again= input("Type 'yes' to continue , type 'no' to exit \n:")
    if play_again == 'no':
        wanna_end = True
        print("Have a nice day! , Byeee....")





