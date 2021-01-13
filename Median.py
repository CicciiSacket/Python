"""
Visualizza la mediana di un insieme di numeri letti da un file
"""
fileName = input("Enter the file name: ")
f = open(fileName, 'r')

numbers = []
for line in f:
    words = line.split()
    for word in words:
        numbers.append(float(word))

numbers.sort()
midpoint = len(numbers)//2
if len(numbers) % 2 == 1:
    print(numbers[midpoint])
else:
    print((numbers[midpoint] + numbers[midpoint - 1]) / 2)