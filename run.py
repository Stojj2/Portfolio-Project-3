from words import GAME_WORDS


class Game:
    """
    Game class with score and username
    """

    def __init__(self):
        """
        Properties of the game
        """
        self.__name__ = None
        self.__score__ = 0

    def start(self):
        """
        Starts the game, displays the first word from the GAME_WORDS list.
        """
        self.__name__ = name_input()
        for i in GAME_WORDS:
            print("_________________________________________")
            print(f"Question   Score")
            print(f"   {GAME_WORDS.index(i) + 1}         {self.__score__}")
            print(f"Chemical element with the symbol = {i['symbol']}")
            option_list = i['options']
            for x in range(len(option_list)):
                print(option_list[x])

            guessed_answer = answer_input()
            if int(guessed_answer) == int(i['correct_option']):
                self.__score__ += 1
                print(f"\033[1;32mCorrect answer\033[0m")
                print("_________________________________________")
            else:
                print(f"\033[1;31mIncorrect answer\033[0m")
                print("_________________________________________")

    def end(self):
        print(f"Well done {self.__name__},\nYou scored {self.__score__}/5")


def preparation():
    """
    Showing a welcome message to the user
    """
    print("\n\n\033[1mWelcome to Element Guesser\033[0m")


def name_input():
    """
    Asks the user to input a name and checks if the data is valid

    Returns:
        The return value is the name of the user
    """
    while True:
        print("_________________________________________")
        print("Choose name, max 10 characters")

        x = str(input('Enter name: \n'))
        if len(x) <= 10 and len(x) >= 1:
            print("Great choice, Let's begin!")
            print("_________________________________________")
            return x
        else:
            print('\033[4;31mName need to be between 1-10 characters\033[0;m')


def answer_input():
    """
    Asks the user to input a answer number and checks if the data is valid

    Returns:
        The return value will be an integer.
        The integer have been validated to be between 1-3
    """
    while True:
        try:
            x = int(input("\nEnter number and press enter: \n"))
            if x <= 3 and x >= 1:
                return x
            else:
                print("\033[4;31m Integer must be between 1-3! \033[0;m")
        except ValueError:
            print('\033[4;31m Input needs to be a integer! \033[0;m')


def main():
    """
    Run all game functions
    """
    preparation()
    game = Game()
    game.start()
    game.end()


if __name__ == "__main__":
    main()
