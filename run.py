# Write your code to expect a terminal of 80 characters wide and 24 rows high
from words import GAME_WORDS

class Game:
    """
    Game class with score and username
    """
    def __init__(self):
        #properties
        self.__name__ = None
        self.__score__ = 0

    def start(self):
        """
        Starts the game, displays the first word from the game list passed in word_list variable.
        """
        for i in GAME_WORDS:
            print("_______________________________________________________________________________")
            print("Chose a option from bellow")
            print(i['options'])
            guessed_answer = answer_input()
            if int(guessed_answer) == int(i['correct_option']):
                print("you guessed right")
                self.__score__ += 1
                print(f"                                                                        Score {self.__score__}")
            else:
                print("wrong answer")
                print(f"                                                                        Score {self.__score__}")
                print("_______________________________________________________________________________")
        print(f"GAME OVER\nYour scored {self.__score__}/5")


def preparation():
    """
    Showing a welcome message to the user
    """
    print("Welcome to Element guesser")

def name_input():
    """
    Asks the user to input a name and checks if the data is valid
    """
    while True:
        print("-------------------------------------------------------------------------------")
        print("Choose name, max 10 letters")

        x = str(input('Enter name: \n'))
        if len(x) <= 10 and len(x) >= 0:
            print("Great choice!")
            print("-------------------------------------------------------------------------------")
            return x
        else:
            print('\033[4;31m Name must be characters with a max lenght of 10 \033[0;m')

def answer_input():
    """
    Asks the user to input a answer number and checks if the data is valid
    """
    while True:
        try:
            x = int(input("\nEnter number and press enter: \n"))
            if x <= 3 and x >= 1:
                return x
            else:
                print("\033[4;31m Integer must be between 1-3, try again! \033[0;m")
        except ValueError:
            print('\033[4;31m Input needs to be a integer, try again! \033[0;m')

def start(self):
    """
    Starts the game, displays the first word from the game list passed in word_list variable.
    """
    for i in GAME_WORDS:
        print(f"Chose a option from bellow")
        print(i['options'])
        guessed_answer = answer_input()

        if int(guessed_answer) == int(i['correct_option']):
            print("you guessed rihgt")
            game_1.score += 1
        else:
            print("wrong answer")

def main():
    """
    Run all game functions
    """
    preparation()
    game = Game()
    game.start()

main()