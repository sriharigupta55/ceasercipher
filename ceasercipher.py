class ceasercipher:
    def encryption(self,b,a):
        encoded = ""
        for i in range(len(b)):
          encoded += chr((ord(b[i].upper()) + a - 65) % 26 + 65)
        return encoded
    def decryption(self,b,a):
        decoded = ""
        for i in range(len(b)):
          decoded += chr((ord(b[i].upper()) - a - 65) % 26 + 65)
        return decoded
cl = ceasercipher()
key = int(input("enter key: "))
data = input("enter value: ").replace(" ","")
option = input("enter e if encrypt or to decrypt d else both: ")
if(option=="e"):
    print(cl.encryption(data,key))
elif(option=="d"):
    print(cl.decryption(data,key))
else:
    print(cl.decryption(cl.encryption(data,key),key))
