from margin_separator_module import get_margin_separator
from anagram_gameboard import AnagramGameboard
from pprint import pprint

## BEGIN
class AnagramHunt():
    """ The Anagram Hunt game """
    
    margin_str = get_margin_separator()

    
    def __init__(self):
        """ Creates the Anagram Hunt game's start page """
        super().__init__()


    def welcome_player(self):
        print(self.margin_str)
        print("Welcome to Anagram Hunt!")
        print(self.margin_str)
        print("How many anagrams can you find in 60 seconds?")
        print(self.margin_str)


    def select_word_length(self):
        word_length = 0
        error_msg = "is not a number from 5 through 8."
        while(word_length < 5 or word_length > 8):
            try:
                word_length = int(
                    input("To start, please select a word length, [5, 6, 7, or 8 characters]: ")
                )
            except ValueError:
                print(f"{self.margin_str}\n{word_length} {error_msg}\n{self.margin_str}")
            else:
                if(word_length < 5 or word_length > 8):
                    print(f"{self.margin_str}\n{word_length} {error_msg}\n{self.margin_str}")
        return word_length

    
    def create_gameboard(self, word_length):
        gameboard = AnagramGameboard(word_length)
        return gameboard
## END class

""" To run `anagram_hunt.py` stand-alone/individually """
def main():
    game = AnagramHunt()
    game.welcome_player()
    word_length = game.select_word_length()
    gameboard = game.create_gameboard(word_length)
    gameboard.introduce_game()
    # print("List of lists:\n", "-" * 25)
    # pprint(gameboard.set_word_lists())
    # print("Word List:\n", "-" * 25)
    # pprint(gameboard.set_word_list())
    # print(gameboard.set_anagram_word())
    # gameboard.ask_question()
    gameboard.start_game()


if(__name__ == "__main__"):
    main()