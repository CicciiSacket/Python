sentences = int(input("sentences: "))
words = int(input("words: "))
syllables = int(input("syllables: "))

index = 206.835 - 1.015 * (words/sentences) - 84.6 * (syllables/words)
print("Flash index: ", index)

level = round(0.39 * (words/sentences) + 11.8 * (syllables/words) - 15.59)
print("Grade level:", level)