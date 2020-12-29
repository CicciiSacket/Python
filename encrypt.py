#cifratura usando il cifrario di cesare, in input la parola e la distanza nel cifrario di cesare

plainText = input("Enter a one-word, lowercase message: ") 
distance = int(input("Enter the distance value: "))
code = ""

for ch in plainText:
    ordValue = ord(ch)
    cipherValue = ordValue + distance
    if cipherValue > ord('z'):
        cipherValue = ord('a') + distance - (ord('z') - ordValue - 1)
    code += chr(cipherValue)
print(code)