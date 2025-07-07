#example conversione da esadecimale a binario
hexToBinaryTable = {
    '0':'0000', '1':'0001','2':'0010', '3':'0011',
    '4':'0100', '5':'0101','6':'0110', '7':'0111',
    '8':'1000', '9':'1001','A':'1010', 'B':'1011',
    'C':'1100', 'D':'1101','E':'1110', 'F':'1111'
}

def convert(number,table):
    binary = ''
    for digit in number:
        binary+= table[digit]
    return binary
print(convert("35A",hexToBinaryTable))

#trovare la moda di un elenco di valori
fileName = input("Enter the file name: ")
f = open(fileName,'r')

words = []
for line in f:
    for word in line.split():
        words.append(word.upper())

theDictionary = {}
for word in words:
    number = theDictionary.get(word,None)
    if number == None:
        theDictionary[word] = 1
    else:
        theDictionary[word] = number + 1

theMaximum = max(theDictionary.values())
for key in theDictionary:
    if theDictionary[key] == theMaximum:
        print("The mode is", key)
        break
