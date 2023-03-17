# Write your code to expect a terminal of 80 characters wide and 24 rows high
from words import *


class Game:
   """
   Game class
   """
   def __init__(self, name, category, score, counter):
      #properties
       self.name = name
       self.category = category
       self.score = score
       self.counter = counter

   #behaviour
   def description(self):
       """
       describe the game
       """
       return f"{self.name} scored {self.score} in game category {self.category}" 
       
def preparation():
    """
    Loading highscore data from CSV and displays a welcome message
    """
    print("Welcome to Words The Chemist")

def category_input():
    """
    Asks the user to input a category number and checks if the data is valid
    """
    while True:
        print("_______________________________________________________________________________")
        print("Chose a number from the categories below\n")
        print("1 - Chemical elements - names")
        print("2 - Chemical elements - symbols")

        try:
            x = int(input("\nEnter number and press enter: \n"))
            if x <= 2 and x >= 1:
                print("Great choice!")
                return x
            else:
                print("\033[4;31m Integer must be between 1-2 \033[0;m")
        except ValueError:
            print('\033[4;31m Input needs to be a integer, try again! \033[0;m')


def name_input():
    """
    Asks the user to input a name and checks if the data is valid
    """
    while True:
        print("-------------------------------------------------------------------------------")
        print("We do also need your name")
        print("choose name, max 10 letters")

        x = str(input('Enter name: \n'))
        if len(x) <= 10 and len(x) >= 0:
            print("Great choice!")
            print("-------------------------------------------------------------------------------")
            return x
        else:
            print('\033[4;31m Name must be characters with a max lenght of 10 \033[0;m')
    

def validate_integer(input):
    """
    Validates the data typed in by the player
    """

def start_game(word_list):
    """
    Starts the game, displays the first word from the game list passed in word_list variable.
    """


def main():
    """
    Run all game functions
    """
    game_1 = Game('no_name', 'Chemical elements - names', 0, 10)
    game_2 = Game('no_name', 'Chemical elements - symbols', 0, 10)
    preparation()
    game_category = category_input()
    game_name = name_input()


main()