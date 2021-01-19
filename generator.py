#generare frasi dato un vocabolario definito con il tipo "tupla"
import random 

articles = ("A","THE")
nouns = ("BOY","GIRLS","BAT","BALL")
verbs = ("HIT","SAW","LIKED")
preposition = ("WITH","BY")

def sentence():
    return nounPhrase() + " " + verbPhrase()+ "."

def nounPhrase():
    return random.choice(articles) + " " +random.choice(nouns)

def verbPhrase():
    return random.choice(verbs) + " " + nounPhrase() + " " + prepositionalPhrase()

def prepositionalPhrase():
    return random.choice(preposition) + " " + nounPhrase()

def main():
    number = int(input("Enter the number of sentences: "))
    for count in range(number):
        print(sentence())

if __name__ == "__main__":
    main()