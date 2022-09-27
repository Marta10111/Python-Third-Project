from pyfiglet import Figlet
from termcolor import colored

def start():
    """
    Game starts with message and options
    """
    print("Welcome to the Horror Movie Quiz")

    f = Figlet(font = 'poison')
    print(colored(f.renderText('Horrorland'), 'red'))


start()



