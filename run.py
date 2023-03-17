# Your code goes here.
# You can delete these comments, but do not change the name of this file
# Write your code to expect a terminal of 80 characters wide and 24 rows high

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
    print("\nWelcome to Words The Chemist\n\nCategory \n1 - Chemical elements - names\n2 - Chemical elements - symbols\n")

def category_input():
    """
    Ask user to choose from 2 categories and returns a list of 10 words from the category choosen.
    """
    category = input("Enter your category number here:\n")
    return category

def start_game(word_list):
    """
    Starts the game, displays the first word from the game list passed in word_list variable.
    Sets the score to 0.
    sets the counter to 10.
    """


def main():
    """
    Run all game functions
    """
    game_1 = Game('no_name', 'Chemical elements - names', 0, 10)
    game_2 = Game('no_name', 'Chemical elements - symbols', 0, 10)
    #print(game_1.score)
    preparation()
    category_data = category_input()
    print(category_data)

main()