"""
conduce una sessione interattiva di psicoterapia non direttiva
"""
import random

hedges = ("Please tell me more.", "Many of my patients tell me the same thing.","Please continue.")
qualifiers = ("Why do you say that ", "You seem to think that ","Can you explain why ")
replacements =  {'I':'you', 'me':'you','my':'yours', 'we':'you','us':'you', 'mine':'yours'}

def reply(sentences):
    probability = random.randint(1,4)
    if probability == 1:
        return random.choice(hedges)
    else:
        return random.choice(qualifiers) + changePerson(sentences)

def changePerson(sentences):
    words = sentences.split()
    replyWords = []
    for word in words:
        replyWords.append(replacements.get(word,word))
    return " ".join(replyWords)

def main():
    print("Good mornig, I hope you are well today.")
    print("What can I do for you?")
    while True:
        sentences = input("\n>>")
        if sentences.upper() == "QUIT":
            print("Have a nice day!")
            break
        print(reply(sentences))

if __name__ == "__main__":
    main()

