import colorama
from colorama import Fore, Style
colorama.init(autoreset=True)

quiz_questions = [
    {"question": "What is the name of the camp where Jason Voorhees drowns\
 in the Friday the 13th series?",
     "answer": {"A": "Camp Eden Lake",
                "B": "Camp Crystal Lake",
                "C": "Camp Silver Lake",
                "D": "Camp Diamond Lake"},
     "correct_answer": "B"},
    {"question": "In which film did Annabelle the doll make her debut?",
     "answer": {"A": "Annabelle",
                "B": "The Nun",
                "C": "The Conjuring",
                "D": "Annabelle Comes Home"},
     "correct_answer": "C"},
    {"question": "What is the Exorcist's Demon's Name?",
     "answer": {"A": "Pazuzu",
                "B": "Azazel",
                "C": "Mammon",
                "D": "Lucifer"},
     "correct_answer": "A"},
    {"question": "What arms does Leatherface prefer?",
     "answer": {"A": "Machete",
                "B": "Kitchen knife",
                "C": "The Axe",
                "D": "Chainsaw"},
     "correct_answer": "D"},
    {"question": "In which horror movie does the phrase 'the power of Christ\
 compels you', appears?",
     "answer": {"A": "The Conjuring",
                "B": "The Exorcist",
                "C": "The Omen",
                "D": "The Nun"},
     "correct_answer": "B"},
    {"question": "Who plays the role of Jack Torrence in the movie\
 'The Shining'",
     "answer": {"A": "Danny Lloyd",
                "B": "Danny DeVito",
                "C": "Scatman Crothers",
                "D": "Jack Nicholson"},
     "correct_answer": "D"},
    {"question": "Which of the following movies is not based on a\
 Stephen King novel?",
     "answer": {"A": "The Orphan",
                "B": "IT",
                "C": "Doctor Sleep",
                "D": "Pet Sematary"},
     "correct_answer": "A"},
    {"question": "What is the occupation of Hannibal Lecter in the movie 'The\
 Silence of the Lambs?",
     "answer": {"A": "A Vet",
                "B": "A Psychiatrist",
                "C": "A Tailor",
                "D": "A Teacher"},
     "correct_answer": "B"},
    {"question": "Who rides around on a red tricycle?",
     "answer": {"A": "Chucky",
                "B": "IT",
                "C": "Annabelle",
                "D": "Jigsaw"},
     "correct_answer": "D"},
    {"question": "Which colours is Freddy Krueger's jumper?",
     "answer": {"A": "Red and Green",
                "B": "Green and Blue",
                "C": "Blue and Red",
                "D": "Red and Yellow"},
     "correct_answer": "A"},
]


def start_screen():
    """
    Game starts with quiz title. Gets user name, shows\
    instructions and ask user if he is ready to start the game
    """
    print(f"""{Fore.RED}{Style.BRIGHT}

██╗  ██╗ ██████╗ ██████╗ ██████╗  ██████╗ ██████╗     
██║  ██║██╔═══██╗██╔══██╗██╔══██╗██╔═══██╗██╔══██╗    
███████║██║   ██║██████╔╝██████╔╝██║   ██║██████╔╝    
██╔══██║██║   ██║██╔══██╗██╔══██╗██║   ██║██╔══██╗    
██║  ██║╚██████╔╝██║  ██║██║  ██║╚██████╔╝██║  ██║    
╚═╝  ╚═╝ ╚═════╝ ╚═╝  ╚═╝╚═╝  ╚═╝ ╚═════╝ ╚═╝  ╚═╝    
                                                      
███╗   ███╗ ██████╗ ██╗   ██╗██╗███████╗███████╗      
████╗ ████║██╔═══██╗██║   ██║██║██╔════╝██╔════╝      
██╔████╔██║██║   ██║██║   ██║██║█████╗  ███████╗      
██║╚██╔╝██║██║   ██║╚██╗ ██╔╝██║██╔══╝  ╚════██║      
██║ ╚═╝ ██║╚██████╔╝ ╚████╔╝ ██║███████╗███████║      
╚═╝     ╚═╝ ╚═════╝   ╚═══╝  ╚═╝╚══════╝╚══════╝      
                                                      
         ██████╗ ██╗   ██╗██╗███████╗                 
        ██╔═══██╗██║   ██║██║╚══███╔╝                 
        ██║   ██║██║   ██║██║  ███╔╝                  
        ██║▄▄ ██║██║   ██║██║ ███╔╝                   
        ╚██████╔╝╚██████╔╝██║███████╗                 
         ╚══▀▀═╝  ╚═════╝ ╚═╝╚══════╝ 

""")


start_screen()

name = input("Please type your Name and hit the enter key:\n")

while not name.strip():
    print("Please enter your Name to start\n")
    name = input("Please type your Name and hit the enter key:\n")
else:
    print(f"Welcome to Horror Movie Quiz {name}!\n")
    print("Take the quiz to test your knowledge of popular horror movies.\n")
    print("There are 10 multiple choice questions.\n")
    print("Select your answer by typing 'a', 'b', 'c' or 'd'.\n")
    print("Good luck!\n")

start_quiz = True

while start_quiz:
    commence_quiz = input("Are you ready to start? y/n\n")

    if commence_quiz.lower() == "y":
        print("Great!\n")
        break
    elif commence_quiz.lower() == "n":
        print("Type 'y' if you are ready to start\n")
    else:
        print("Please type y or n\n")


def run_game(quiz_questions):
    """
    Shows quiz questions and answers, add 1 score for correct answer or none\
    for wrong answer
    """
    score = 0
    for entry in quiz_questions:
        user_answer = ''
        while user_answer not in ['A', 'B', 'C', 'D']:
            print(f"{Fore.BLUE}{Style.BRIGHT}{entry['question']}")

            for key, value in entry['answer'].items():
                print(f"\t{key}: {value}")

            user_answer = input("Type your answer?\n")
            user_answer = user_answer.upper()

            if user_answer not in entry['answer']:
                print("Only a, b, c or d are accepted\n")

        if user_answer == entry['correct_answer']:
            print(f"{Fore.GREEN}You're right\n")
            score += 1
        else:
            print(f"{Fore.RED}You're wrong\n")

    final_score(score)


def final_score(score):
    """
    Display final score at the end of quiz
    """
    if score <= 5:
        print(f"You know nothing {name}! Your final score is {score} out of\
 10. Better luck next time.")
        print("Take the quiz again to see if you can improve your score.\n")
    elif score > 5:
        print(f"Well done {name}! Your final score is {score} out of\
 10. You are a true Horror Movie fan.")


def play_again():
    """
    Ask user if they want to play again. If yes- returns to the quiz\
    start, if not quiz ends
    """

    restart_quiz = True

    while restart_quiz:
        response = input("Do you want to play again? y/n\n")
        response = response.upper()

        if response == "Y":
            return True
        elif response == "N":
            return False
        else:
            print("Please type 'Y' if you want start again, or 'N'\
            if you want to quit \n")


start_screen()
run_game(quiz_questions)


while play_again():
    start_screen()
    run_game(quiz_questions)
else:
    print("The End\nThank you for playing")
    print("click the 'RUN PROGRAM' button to reset the quiz")
    