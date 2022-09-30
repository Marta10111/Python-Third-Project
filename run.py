import pyfiglet
from termcolor import colored


def start_screen():
    """
    Game starts with quiz title. Gets user name, shows\
    instructions and ask user if he is ready to start the game    
    """
    print(colored(pyfiglet.figlet_format('Horror\
    Movie Quiz', font='poison'), 'red'))


start_screen()

NAME = input("Please type your name and hit the enter key:\n")
while not NAME.strip():
    print("Please enter your name to start\n")
    NAME = input("Please type your name and hit the enter key")

else:
    print(f"Welcome to Horror Movie Quiz {NAME}!\n")
    print("Take the quiz to test your knowledge of popular horror movies.\n")
    print("There are 10 multiple choice questions.\n")
    print("Select your answer by typing 'a', 'b', 'c' or 'd'.\n")
    print("Good luck!\n")
    
  
commence_quiz = input("Are you ready to start? y/n\n")
if commence_quiz.lower() == "y":
    print("Great!\n")
elif commence_quiz.lower() == "n":
    print("Type 'y' if you are ready to start\n")
else:
    print("Please type y or n\n")   

"""
Defining score Variables
"""
score = 0

"""
Question one
"""
print("What is the name of the camp where Jason Voorhees drowns in the Friday\
the 13th series?")
answer_1 = input("a) Camp Eden Lake\nb) Camp Crystal Lake\nc) Camp Silver Lake\
\nd) Camp Diamond Lake\n")
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
answer_2 = input("a) Annabelle\nb) The Nun\nc) The Conjuring\nd) Annabelle\
Comes Home\n")
if answer_2 == "c":
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
print("In which horror movie does the phrase 'the power of Christ compels you'\
, appears?")
answer_5 = input("a) The Conjuring\nb) The Exorcist\nc) The Omen\nd) The Nun\
\n")
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

"""
Question six
"""
print("Who plays the role of Jack Torrence in the movie 'The Shining'?")
answer_6 = input("a) Danny Lloyd\nb) Danny DeVito\nc) Scatman Crothers\nd)\
 Jack Nicholson\n")
if answer_6 == "d":
    print("Answer:", answer_6)
    score = score + 1
    print("You're right")
    print("score:", score)
    print("\n")
else:
    print("You're wrong, the answer is d")
    print("score:", score)
    print("\n")

"""
Question seven
"""
print("Which of the following movies is not based on a Stephen King novel?")
answer_7 = input("a) The Orphan\nb) IT\nc) Doctor Sleep\nd) Pet Sematary\n")
if answer_7 == "a":
    print("Answer:", answer_7)
    score = score + 1
    print("You're right")
    print("score:", score)
    print("\n")
else:
    print("You're wrong, the answer is a")
    print("score:", score)
    print("\n")

"""
Question eight
"""
print("What is the occupation of Hannibal Lecter in the movie 'The Silence of\
the Lambs?")
answer_8 = input("a) A Vet\nb) A Psychiatrist\nc) A Tailor\nd) A Teacher\n")
if answer_8 == "b":
    print("Answer:", answer_8)
    score = score + 1
    print("You're right")
    print("score:", score)
    print("\n")
else:
    print("You're wrong, the answer is b")
    print("score:", score)
    print("\n")

"""
Question nine
"""
print("Who rides around on a red tricycle?")
answer_9 = input("a) Chucky\nb) IT\nc) Annabelle\nd) Jigsaw\n")
if answer_9 == "d":
    print("Answer:", answer_9)
    score = score + 1
    print("You're right")
    print("score:", score)
    print("\n")
else:
    print("You're wrong, the answer is d")
    print("score:", score)
    print("\n")

"""
Question ten
"""
print("Which colours is Freddy Krueger's jumper?")
answer_10 = input("a) Red and Green\nb) Blue and Green\nc) Yellow and Red\n\
d) Yellow and Green\n")
if answer_10 == "a":
    print("Answer:", answer_10)
    score = score + 1
    print("You're right")
    print("score:", score)
    print("\n")
else:
    print("You're wrong, the answer is a")
    print("score:", score)
    print("\n")

""" 
Display final score at the end of quiz
"""
if score <= 5:
    print(f"You know nothing {NAME}! Your final score is {score} out of\
 10. Better luck next time.")
    print("Take the quiz again to see if you can improve your score.\n")
elif score > 5:
    print(f"Well done {NAME}! Your final score is {score} out of\
 10. You are a true Horror Movie fan.")