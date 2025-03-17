import sys
import os
project_root = os.path.abspath(os.path.join(os.path.dirname(__file__), '..'))
sys.path.insert(0, project_root)
from helpers.margin_separator_module import get_margin_separator
from anagram_game.anagram_gameboard import AnagramGameboard


## BEGIN
class AnagramHunt():
    """ The Anagram Hunt game """

    
    def __init__(self):
        """ Creates the Anagram Hunt game's start page """
        super().__init__()
        self._MARGIN_STR = get_margin_separator()
        ## Python convention of explicitly returning, even if empty, to mark the end of a method.
        return


    def welcome_player(self):
        print(self._MARGIN_STR)
        print("Welcome to Anagram Hunt!")
        print(self._MARGIN_STR)
        print("How many anagrams can you find in 60 seconds?")
        print(self._MARGIN_STR)
        return


    def select_word_length(self):
        word_length = 0
        ERROR_MSG = "is not a number from 5 through 8."
        while(word_length < 5 or word_length > 8):
            try:
                word_length = int(
                    input("To start, please select a word length, [5, 6, 7, or 8 characters]: ")
                )
            except ValueError:
                print(f"{self._MARGIN_STR}\n{word_length} {ERROR_MSG}\n{self._MARGIN_STR}")
            else:
                if(word_length < 5 or word_length > 8):
                    print(f"{self._MARGIN_STR}\n{word_length} {ERROR_MSG}\n{self._MARGIN_STR}")
        return word_length

    
    def create_gameboard(self, word_length=5):
        gameboard = AnagramGameboard(word_length)
        return gameboard
## END class


## To run `anagram_hunt.py` stand-alone/individually
def main():
    game = AnagramHunt()
    game.welcome_player()
    word_length = game.select_word_length()
    gameboard = game.create_gameboard(word_length)
    gameboard.introduce_game()
    gameboard.start_game()
    return


if(__name__ == "__main__"):
    main()