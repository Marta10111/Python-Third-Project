from pyfiglet import Figlet
from termcolor import colored

def start():
    """
    Game starts with message and options
    """
    print("Welcome to the Horror Movie Quiz")

    f = Figlet(font='poison')
    print(colored(f.renderText('Horrorland'), 'red'))

start()

"""
Defining score Variables
"""
score = 0

"""
Question one
"""
print("What is the name of the camp where Jason Voorhees drowns in the Friday the 13th series?")
answer_1 = input("a) Camp Eden Lake\nb) Camp Crystal Lake\nc) Camp Silver Lake\nd) Camp Diamond Lake\n")
if answer_1 == "b":
    print("Answer:", answer_1)
    score = score + 1
    print("You're right")
    print("score:", score)
    print("\n")
else:
    print("You're wrong, the answer is b")
    print("score:", score)
    print("\n")

"""
Question two
"""
print("In which film did Annabelle the doll make her debut?")
answer_2 = input("a) Annabelle\nb) The Nun\nc) The Conjuring\nd) Annabelle Comes Home\n")
if answer_1 == "c":
    print("Answer:", answer_2)
    score = score + 1
    print("You're right")
    print("score:", score)
    print("\n")
else:
    print("You're wrong, the answer is c")
    print("score:", score)
    print("\n")

"""
Quesation three
"""
print("What is the Exorcist's Demon's Name?")
answer_3 = input("a) Pazuzu\nb) Azazel\nc) Mammon\nd) Lucifer\n")
if answer_3 == "a":
    print("Answer:", answer_3)
    score = score + 1
    print("You're right")
    print("score:", score)
    print("\n")
else:
    print("You're wrong, the answer is a")
    print("score:", score)
    print("\n")

"""
Question four
"""
print("What arms does Leatherface prefer?")
answer_4 = input("a) Machete\nb) Kitchen Knife\nc) The Axe\nd) Chainsaw\n")
if answer_4 == "d":
    print("Answer:", answer_4)
    score = score + 1
    print("You're right")
    print("score:", score)
    print("\n")
else:
    print("You're wrong, the answer is d")
    print("score:", score)
    print("\n")

"""
Question five
"""
print("In which horror movie does the phrase 'the power of Christ compels you', appears?")
answer_5 = input("a) The Conjuring\nb) The Exorcist\nc) The Omen\nd) The Nun\n")
if answer_5 == "b":
    print("Answer:", answer_5)
    score = score + 1
    print("You're right")
    print("score:", score)
    print("\n")
else:
    print("You're wrong, the answer is b")
    print("score:", score)
    print("\n")




