#calcola e visualizza indice di flash e livello scolastgico equivalente

#Aquisizione dati
fileName = input("Enter the file name: ")
inputFile = open(fileName,'r')
text = inputFile.read()

#conteggio frasi, parole e sillabe
sentences = text.count('.') + text.count('?') + text.count(':') + text.count(';') + text.count('!')
words = len(text.split())
syllables = 0
vowels = "aeiouAEIOU"
for word in text.split():
    for vowel in vowels:
        syllables += word.count(vowel)
    for ending in ['es','ed','e']:
        if word.endswith(ending):
            syllables -= 1
    if word.endswith('le'):
        syllables +=1

index = 206.835 - 1.015 * (words/sentences) - 84.6 * (syllables/words)
level = round(0.39 * (words/sentences) + 11.8 * (syllables/words) - 15.59)

print("The flash index is: ",index)
print("The GLE is: ", level)
print("Sentences ", sentences)
print("Words ", words)
print("syllables ", syllables)





