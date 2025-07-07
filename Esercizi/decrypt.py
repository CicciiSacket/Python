#decprypt of encrypt.py 

code = input("Enter the coded text: ")
distance = int(input("Enter the distance value: "))
decode = ""

for ch in code:
    ordValue = ord(ch)
    plainValue = ordValue - distance
    if plainValue < ord('a'):
        plainValue = ord('z') - (distance - (ord('a') - ordValue - 1))
    decode += chr(plainValue)
print(decode)