text='abcdefghijklmnopqrstuvwxyz'
string=input("Enter a message to be encrypted : ")
key=int(input("Enter a key : "))
encryptedKey=''
for i in string:
    p=text.find(i)
    newpos=(p+key)%26
    char=text[newpos]
    encryptedKey+=char
print("Secret Message Generated :",encryptedKey)