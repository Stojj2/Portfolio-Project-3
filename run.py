# Write your code to expect a terminal of 80 characters wide and 24 rows high
from words import *
from collections import OrderedDict


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
    print("Welcome to Element guesser")


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


def start_game(category, name):
    """
    Starts the game, displays the first word from the game list passed in word_list variable.
    """
    if category == 1:
        print(f"Hi {name}, you will get the chemical element symbol an will have to guess what element name it has\n")

        for i in game_words:
            game_1 = Game(name, 'Chemical elements - names', 0, 10)
            symbol = game_words[i]['symbol']
            options = game_words[i]['alternative_name']
            options.append(game_words[i]['name'])
            print(f'What name does the element symbol {symbol} has')
            print(options)
            input("answer:\n")
            print("\n")
            print(f'Your Score is {game_1.score} and you are at question {i}/{game_1.counter}')
            print("-------------------------------------------------------------------------------")
            
    elif category == 2:
        print(f"Hi {name}, you will get the chemical element name an will have to guess what symbol it has")    


def main():
    """
    Run all game functions
    """
    preparation()
    game_category = category_input()
    game_name = name_input()
    start_game(game_category, game_name)


main()