#pip install pycryptodome
from Crypto.Util.number import inverse

n = int(input("Enter 'n' : "))
print("\n+++++ If p and q are not known, go to http://factordb.com/ and factorise n +++++")
p = int(input("Enter 'p' : "))
q = int(input("Enter 'q' : "))
e = int(input("Enter 'e' : "))
cipher_text = int(input("\nPlace Cipher Text Here : "))

#Euler Totient Function
piofn = (p-1)*(q-1)

#Inverse Modulo Of Piofn
d = inverse(e,piofn)

#Decrypt The Cipher Text
plain_text = pow(cipher_text,d,n)

#get the value of flag in hex
hex_string = hex(plain_text)[2:] #remove 0x from output

#hex to bytes
bytes_object = bytes.fromhex(hex_string)

#bytes to ascii
ascii_string = bytes_object.decode("ASCII")

#print the value of flag in ascii
print("\nflag : ", ascii_string)

